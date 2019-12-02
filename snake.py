import pygame
from main_window import *
from utils import *


# SNAKE #
class Snake:
	def __init__(self, x, y, size, speed, color):
		self.x = x
		self.y = y
		self.init_tail()
		self.size = size
		self.color = color
		self.speed = speed
		self.velocity = [0, 0]
		self.direction = 'S'
		self.img = pygame.image.load(SNAKE_HEAD_IMG)
		self.head_img = self.img
	
	def init_tail(self):
		self.tail = []
		for i in range(0, SNAKE_INIT_LENGTH - 1):
			self.tail.append([0, 0])
	
	def __len__(self):
		return len(self.snake_tiles)
	
	def rotate_head(self):
		if self.direction == 'R':
			self.head_img = pygame.transform.rotate(self.img, 270)
		elif self.direction == 'L':
			self.head_img = pygame.transform.rotate(self.img, 90)
		elif self.direction == 'U':
			self.head_img = self.img
		elif self.direction == 'D':
			self.head_img = pygame.transform.rotate(self.img, 180)
	
	def draw(self):
		#pygame.draw.rect(window, self.color, [self.x, self.y, self.size, self.size])
		window.blit(self.head_img, (self.x, self.y))
		for tile_location in self.tail:
			pygame.draw.rect(window, self.color, [tile_location[0], tile_location[1], self.size, self.size])
			
	def update(self):
		window.blit(self.head_img, (self.x, self.y))
		self.rotate_head()
		for i in range(0, len(self.tail) - 1):
			self.tail[i] = self.tail[i + 1]
		if len(self.tail) > 0:
			self.tail[-1] = [self.x, self.y]
		self.x += self.velocity[0]
		self.y += self.velocity[1]
			
	def set_direction(self, direction):
		self.direction = direction
		if direction == 'L':
			self.velocity = [-self.speed, 0]
		if direction == 'R':
			self.velocity = [self.speed, 0]
		if direction == 'U':
			self.velocity = [0, -self.speed]
		if direction == 'D':
			self.velocity = [0, self.speed]
		
	def get_direction(self):
		return self.direction
		
	def stop(self):
		self.direction = 'S'
		self.velocity = [0, 0]
			
	def lengthen(self):
		self.tail.append([self.x, self.y])
		
	def collide_frame(self, board):
		check_x_axis = self.x < board.x or self.x >= board.x + board.width
		check_y_axis = self.y < board.y or self.y >= board.y + board.height
		return check_x_axis or check_y_axis
		
	def check_self_collision(self):
		if self.direction == 'S':
			return False
		for i in range(0, len(self.tail) - 1):
			pos = self.tail[i]
			if self.x == pos[0] and self.y == pos[1]:
				return True
		return False

	def collide_food(self, food):
		x_axis = self.x == food.x 
		y_axis = self.y == food.y 
		#x_axis = self.x >= food.x and self.x <= food.x + food.size
		#y_axis = self.y >= food.y and self.y <= food.y + food.size
		return x_axis and y_axis
