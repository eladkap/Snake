import pygame
from main_window import *

# FOOD #
class Food:
	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		self.img = pygame.image.load(APPLE_IMG)
		
	def draw(self):
		pygame.draw.rect(window, self.color, [self.x, self.y, self.size, self.size])
		window.blit(self.img, (self.x, self.y))
