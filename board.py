import pygame
from main_window import *

# BOARD #
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
