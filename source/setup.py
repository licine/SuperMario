import pygame
# from . import constants as C
# from . import tools
from source import constants as C
from source import tools

pygame.init()
SCREEN = pygame.display.set_mode(C.SCREEN_SIZE)

GRAPHICS = tools.load_graphics('resources/graphics')
