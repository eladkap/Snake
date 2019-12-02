import os
import sys
import pygame
from settings import *


# Change current directoy to main script location #
os.chdir(os.path.dirname(sys.argv[0]))
print(os.getcwd())

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Snake')
pygame.font.init()

icon = pygame.image.load(APPLE_IMG)
pygame.display.set_icon(icon)
