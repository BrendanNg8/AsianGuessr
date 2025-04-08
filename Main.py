import pygame
import sys
import os
from playerClass import Player


#FOR BUTTONS, WE USING LUCIDA CALIGRAPHY FONT IN MICROSOFT PAINT

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
clicked_start = False

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
#FIGHTERS

player1 = Player(200, 375)
player2 = Player(700, 375)

#------------------------------
x = pygame.Rect(50, 50, 300, 300)
backupStart = pygame.draw.rect(screen, (255,0,0), x)

running = True
while running:
    #--------------------------
    #Drawing
    draw_bg()
    
    if clicked_start == True:
        player1.draw(screen)
        player2.draw(screen)
        player1.move()
    while clicked_start != True:
        draw_PB()
    #--------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
        if playButton.rect.collidepoint(mouse_pos):
            clicked_start = True
    pygame.display.update()
    clock.tick(60) #Don't run more than 60 times a second

pygame.quit()
sys.exit()

    


