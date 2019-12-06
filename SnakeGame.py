import pygame
from tkinter import *
from tkinter import messagebox
import random
import math
import time

from main_window import *
from button import *
from board import *
from snake import *
from food import *
from settings import *
from utils import *


class SnakeGame:
	def __init__(self):
		self.init()

	def init(self):
		self.game_over = False
		self.game_quit = False
		self.menu_flag = True
		self.game_controls_flag = False
		self.score = 0
		self.board = Board(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT, BOARD_COLOR, BOARD_THICKNESS)
		self.position_snake()
		self.generate_food()
		self.set_buttons()
		
	def set_buttons(self):
		self.btn_play = Button(50, 500, 100, 50, 'PLAY', 'Arial', 20, BLACK, GREEN, LIGHT_GREEN)
		self.btn_controls = Button(200, 500, 100, 50, 'CONTROLS', 'Arial', 20, BLACK, GREEN, LIGHT_GREEN)
		self.btn_main = Button(350, 500, 100, 50, 'MAIN', 'Arial', 20, BLACK, GREEN, LIGHT_GREEN)
		self.btn_quit = Button(500, 500, 100, 50, 'QUIT', 'Arial', 20, BLACK, GREEN, LIGHT_GREEN)
		
	def position_snake(self):
		snake_i = random.randrange(0, BOARD_ROWS)
		snake_j = random.randrange(0, BOARD_COLS)
		snake_x = snake_i * TILE_SIZE + self.board.x
		snake_y = snake_j * TILE_SIZE + self.board.y
		self.snake = Snake(snake_x, snake_y, TILE_SIZE, SNAKE_SPEED, SNAKE_COLOR)
		
	def generate_food(self):
		food_i = random.randrange(0, BOARD_ROWS)
		food_j = random.randrange(0, BOARD_COLS)
		food_x = food_i * TILE_SIZE + self.board.x
		food_y = food_j * TILE_SIZE + self.board.y
		self.food = Food(food_x, food_y, APPLE_SIZE, APPLE_COLOR)
		
	def check_collision(self):
		if self.snake.collide_frame(self.board) or self.snake.check_self_collision():
			self.game_over = True
			self.board.set_color(RED)
			msg = 'GAME OVER'
			self.show_message(msg, 
							[(SCREEN_WIDTH / 2) - (BIG_FONT * len(msg) / 2), 
							SCREEN_HEIGHT / 2],
							RED,
							FONT_FAMILY1, 
							BIG_FONT,
							True,
							0)
			pygame.display.update()
			time.sleep(GAME_OVER_DELAY)
			
	def check_collision_with_food(self):
		if self.snake.collide_food(self.food):
			self.score += SCORE_PTS_INCREASE
			self.generate_food()
			self.snake.lengthen()
	
	def message_box(self, msg):
		Tk().wm_withdraw()
		messagebox.showinfo('Snake', msg)
		
	def show_message(self, msg, location, color, font_family, font_size, center_flag, y_offset):
		if center_flag:
			text_surface, text_rect = text_objects(msg, color, font_family, font_size)
			text_rect.center = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + y_offset
			window.blit(text_surface, text_rect)
		else:
			font = pygame.font.SysFont(font_family, font_size)
			text = font.render(msg, True, color)
			window.blit(text, location)
	
	def show_states(self):
		self.show_message('SCORE: ' + str(self.score), [STATES_X, STATES_Y], BLACK, FONT_FAMILY1, SMALL_FONT, False, 0)
	
	def start_game(self):
		print('Start game')
		self.routine()
	
	def show_controls(self):
		print('Show controls')
		self.main_flag = False
		self.game_controls_flag = True
		while self.game_controls_flag:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
		
			window.fill(WHITE)
			self.show_message('Game Controls', [0, 0], BLACK, FONT_FAMILY1, HUGE_FONT, True, -30)
			self.show_message('Movement: Arrow keys', [0, 0], BLACK, FONT_FAMILY1, MEDIUM_FONT, True, 30)
			self.show_message('Go to Main Screen: ESC', [0, 0], BLACK, FONT_FAMILY1, MEDIUM_FONT, True, 60)
			self.show_message('Pause the Game: P', [0, 0], BLACK, FONT_FAMILY1, MEDIUM_FONT, True, 90)
			
			curr_mouse_pos = pygame.mouse.get_pos()
			self.btn_play.draw(curr_mouse_pos)
			self.btn_main.draw(curr_mouse_pos)
			self.btn_quit.draw(curr_mouse_pos)
			
			# MOUSECLICK #
			click = pygame.mouse.get_pressed()
			if self.btn_play.mouseclick(curr_mouse_pos, click):
				self.start_game()
			if self.btn_quit.mouseclick(curr_mouse_pos, click):
				self.quit()
			if self.btn_main.mouseclick(curr_mouse_pos, click):
				self.show_menu_screen()
			# MOUSECLICK #
			
			pygame.display.update()
			clock.tick(15)
	
	def show_menu_screen(self):
		print('Main screen')
		self.menu_flag = True
		self.game_controls_flag = False
		while self.menu_flag:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()	
		
			window.fill(WHITE)
			self.show_message('Snake', [0, 0], BLACK, FONT_FAMILY1, HUGE_FONT, True, 0)
			
			curr_mouse_pos = pygame.mouse.get_pos()
			self.btn_play.draw(curr_mouse_pos)
			self.btn_controls.draw(curr_mouse_pos)
			self.btn_quit.draw(curr_mouse_pos)
			
			# MOUSECLICK #
			click = pygame.mouse.get_pressed()
			if self.btn_play.mouseclick(curr_mouse_pos, click):
				self.start_game()
			elif self.btn_quit.mouseclick(curr_mouse_pos, click):
				self.quit()
			elif self.btn_controls.mouseclick(curr_mouse_pos, click):
				self.show_controls()
			# MOUSECLICK #
			
			pygame.display.update()
			clock.tick(15)
			
	
	def game_over_loop(self):
		while self.game_over:
			window.fill(WINDOW_BACKCOLOR)
			msg = 'Press SPACE to play again'
			self.show_message(msg,
							[(SCREEN_WIDTH / 2) - (BIG_FONT * len(msg) / 2), 
							SCREEN_HEIGHT / 2],
							BLACK,
							FONT_FAMILY1, 
							BIG_FONT,
							True,
							0)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.reset()
				if event.type == pygame.QUIT:
					self.quit()
						
	
	def routine(self):
		while not self.game_quit:
			# GAME OVER LOOP #
			self.game_over_loop()
			# GAME OVER LOOP #
		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game_quit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.pause()
					elif event.key == pygame.K_LEFT and self.snake.get_direction() != 'R':
						self.snake.set_direction('L')
					elif event.key == pygame.K_RIGHT and self.snake.get_direction() != 'L':
						self.snake.set_direction('R')
					elif event.key == pygame.K_UP and self.snake.get_direction() != 'D':
						self.snake.set_direction('U')
					elif event.key == pygame.K_DOWN and self.snake.get_direction() != 'U':
						self.snake.set_direction('D')
					elif event.key == pygame.K_SPACE:
						self.snake.stop()
					elif event.key == pygame.K_ESCAPE:
						self.show_menu_screen()
					
			window.fill(WINDOW_BACKCOLOR)	
			self.board.draw()
			self.food.draw()
			self.snake.draw()
			self.snake.update()
			self.show_states()
			
			pygame.display.update()
			clock.tick(FPS)
			
			self.check_collision()
			self.check_collision_with_food()		
						
						
	def pause(self):
		game_paused = True
		self.board.set_color(GRAY)
		while game_paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						game_paused = False
						self.board.set_color(BOARD_COLOR)
					elif event.key == pygame.K_q:
						self.quit()
			self.show_message('PAUSED', [0, 0], BLACK, FONT_FAMILY1, BIG_FONT, True, 0)
			self.show_message('Press P to resume game', [0, 0], BLUE, FONT_FAMILY1, MEDIUM_FONT, True, 50)	
			self.board.draw()
			pygame.display.update()
			clock.tick(5)
			
		
	def reset(self):
		self.init()
	
	def quit(self):
		pygame.quit()
		quit()

		
# INITIALIZE GAME #
snake_game = SnakeGame()
# INITIALIZE GAME #

# GAME MENU #
snake_game.show_menu_screen()
# GAME MENU #
