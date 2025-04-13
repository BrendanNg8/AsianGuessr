import pygame
import sys
import os
from playerClass import *
from Constants import *


pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")
clock = pygame.time.Clock()
#------------------------------
#STARTING SCREEN

playButton = pygame.image.load("graphics/playButtons.png").convert_alpha()
def draw_PB():
    scaled_PB = pygame.transform.scale(playButton, (500,300))
    screen.blit(scaled_PB, (250, 375))
#------------------------------
#BACKGROUND
bg_image = pygame.image.load("graphics/castleBG.jpg").convert_alpha()
def draw_bg():
    scaledBG = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaledBG, (0,0))
#------------------------------


#------------------------------

running = True
while running:
    #--------------------------
    #Drawing
    draw_bg()
    
    
    player1.draw(screen)
    player2.draw(screen)
    player1.move(SCREEN_WIDTH)
    
    #--------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.update()
    clock.tick(60) #Don't run more than 60 times a second

pygame.quit()
sys.exit()

    


