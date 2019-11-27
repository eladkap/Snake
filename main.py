import pygame
from tkinter import *
from tkinter import messagebox

from settings import *
import random
import math


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Board:
	def __init__(self, x, y, width, height, color, thickness):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.thickness = thickness
		
	def draw(self):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), self.thickness)
		
	def set_color(self, color):
		self.color = color
	

class Snake:
	def __init__(self, x, y, size, speed, color):
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		self.speed = speed
		self.velocity = (0, 0)
		self.direction = 'S'
	
	def draw(self):
		pygame.draw.rect(window, self.color, [self.x, self.y, self.size, self.size])

	def set_direction(self, direction):
		self.direction = direction
		if direction == 'L':
			self.velocity = (-self.speed, 0)
		if direction == 'R':
			self.velocity = (self.speed, 0)
		if direction == 'U':
			self.velocity = (0, -self.speed)
		if direction == 'D':
			self.velocity = (0, self.speed)
		
	def get_direction(self):
		return self.direction
		
	def stop(self):
		self.direction = 'S'
		self.velocity = (0, 0)
		
	def update(self):	
		self.x += self.velocity[0]
		self.y += self.velocity[1]
		
	def collide_frame(self, board):
		check_x_axis = self.x < board.x or self.x >= board.x + board.width
		check_y_axis = self.y < board.y or self.y >= board.y + board.height
		return check_x_axis or check_y_axis
		
	def collide_food(self, food):
		dest = math.sqrt(abs(self.x - food.x) ** 2 + abs(self.y - food.y) ** 2)
		return dest < 1
	

class Food:
	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		
	def draw(self):
		pygame.draw.rect(window, self.color, [self.x, self.y, self.size, self.size])
	
'''
class Apple:
	def __init__(self, center, radius, color):
		self.center = center
		self.radius = radius
		self.color = color
		
	def draw(self):
		pygame.draw.circle(window, self.color, self.center, self.radius)	
'''
		
class SnakeGame:
	def __init__(self):
		self.init()

	def init(self):
		self.game_over= False
		self.game_quit = False
		self.score = 0
		pygame.init()
		pygame.display.set_caption('Snake')
		self.board = Board(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT, BOARD_COLOR, BOARD_THICKNESS)
		self.position_snake()
		self.generate_food()
		
	def position_snake(self):
		snake_i = random.randint(0, BOARD_ROWS)
		snake_j = random.randint(0, BOARD_COLS)
		snake_x = snake_i * TILE_SIZE + self.board.x
		snake_y = snake_j * TILE_SIZE + self.board.y
		self.snake = Snake(snake_x, snake_y, TILE_SIZE, SNAKE_SPEED, SNAKE_COLOR)
		
	def generate_food(self):
		food_i = random.randint(0, BOARD_ROWS)
		food_j = random.randint(0, BOARD_COLS)
		food_x = food_i * TILE_SIZE + self.board.x
		food_y = food_j * TILE_SIZE + self.board.x
		self.food = Food(food_x, food_y, TILE_SIZE, APPLE_COLOR)
		
	def check_collision_with_frame(self):
		if self.snake.collide_frame(self.board):
			self.board.set_color(RED)
			self.prompt_message('Game Over')
			self.game_over = True
			#self.snake.stop()
			self.reset()
			
	def check_collision_with_food(self):
		if self.snake.collide_food(self.food):
			self.score += SCORE_PTS_INCREASE
			self.generate_food()
	
	def prompt_message(self, msg):
		Tk().wm_withdraw()
		messagebox.showinfo(msg, 'OK')
	
	def routine(self):
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game_quit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and self.snake.get_direction() != 'R':
						self.snake.set_direction('L')
					elif event.key == pygame.K_RIGHT and self.snake.get_direction() != 'L':
						self.snake.set_direction('R')
					elif event.key == pygame.K_UP and self.snake.get_direction() != 'D':
						self.snake.set_direction('U')
					elif event.key == pygame.K_DOWN and self.snake.get_direction() != 'U':
						self.snake.set_direction('D')
					elif event.key == pygame.K_SPACE:
						self.snake.stop()
					
			window.fill(WINDOW_BACKCOLOR)	
			self.board.draw()
			self.snake.draw()
			self.food.draw()
			self.snake.update()
			
			pygame.display.update()
			clock.tick(FPS)
			
			self.check_collision_with_frame()
			self.check_collision_with_food()		
			
			
				
				
	def reset(self):
		self.init()
	
	def quit(self):
		pygame.quit()
		quit()

		
# INITIALIZE GAME #
snake_game = SnakeGame()
# INITIALIZE GAME #

# GAME ROUTINE #
snake_game.routine()
# GAME ROUTINE #
