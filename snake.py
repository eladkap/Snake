import pygame
from main_window import *
import math


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
