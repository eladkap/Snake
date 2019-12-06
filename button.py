import pygame
from main_window import *
from settings import *
from utils import *


class Button:
	def __init__(self, x, y, w, h, text, font_family, font_size, forecolor, backcolor1, backcolor2):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.text = text
		self.font = pygame.font.SysFont(font_family, font_size)
		self.font_size = font_size
		self.font_family = font_family
		self.forecolor = forecolor
		self.backcolor1 = backcolor1
		self.backcolor2 = backcolor2

	def draw(self, mouse_pos):
		if self.mouseover(mouse_pos):
			self.set_backcolor(self.backcolor2)
		else:
			self.set_backcolor(self.backcolor1)
		pygame.draw.rect(window, self.backcolor, (self.x, self.y, self.w, self.h))	
		txt = self.font.render(self.text, True, self.forecolor)	
		text_surf, text_rect = text_objects(self.text, self.forecolor, self.font_family, self.font_size)
		text_rect.center = (self.x + self.w / 2, self.y + self.h / 2)
		window.blit(txt, text_rect)

	def set_backcolor(self, backcolor):
		self.backcolor = backcolor
		
	def mouseclick(self, mouse_pos, click):
		if click[0] == 1:
			x_axis = mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w
			y_axis = mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h
			return x_axis and y_axis
		return False
		
	def mouseover(self, mouse_pos):
		x_axis = mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w
		y_axis = mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h
		return x_axis and y_axis
		