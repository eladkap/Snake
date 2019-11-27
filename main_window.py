import pygame
from settings import *


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Snake')
pygame.font.init()
font = pygame.font.SysFont(None, FONT_SIZE)
