import pygame
from main_window import *


class Food:
	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		
	def draw(self):
		pygame.draw.rect(window, self.color, [self.x, self.y, self.size, self.size])
