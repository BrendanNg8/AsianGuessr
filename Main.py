import pygame
import sys
import os


#FOR BUTTONS, WE USING LUCIDA CALIGRAPHY FONT IN MICROSOFT PAINT

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((2000, 1200))
pygame.display.set_caption("Guess that Asian!")
clock = pygame.time.Clock()

#TODO Put background image -> Load it first so everything else overrides -> (Images drawn in order of written)
playButton = pygame.image.load("graphics/realPB.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.blit(playButton, (0,0)) #Draws my PlayButton
    pygame.display.update()
    clock.tick(60) #Don't run more than 60 times a second

pygame.quit()
sys.exit()

    


