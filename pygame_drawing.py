#import
import pygame, sys
from pygame import display
from pygame.locals import *
#initilize pygame
pygame.init()

#assing fps
FPS = 30
clock = pygame.time.Clock()

#set colurs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#set up display

WIDTH = 300
HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill((212, 183, 140))
pygame.display.set_caption('my drawing')

#creat line and shape
pygame.draw.line(DISPLAYSURF, (255, 0, 255), (150, 130), (130, 170), 3)
pygame.draw.line(DISPLAYSURF, (0, 255, 255), (150, 130), (170, 170), 3)
pygame.draw.line(DISPLAYSURF, GREEN, (130, 170), (170, 170), 3)
pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30, 20)
pygame.draw.circle(DISPLAYSURF, (BLACK), (200, 50), 30, 20)
pygame.draw.rect(DISPLAYSURF, (255,132,56), (100, 200, 100, 50), 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #refreshing
    pygame.display.update()
    clock.tick(FPS)