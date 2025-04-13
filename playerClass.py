import pygame
from Constants import *
import pickle

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x,y, 80, 180))
        self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    #MOVEMENT
    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0 

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        if key(pygame.K_w):
            self.vel_y = -30
        dy += self.val_y

        #ensures play on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        
        #UPDATE POSITION
        self.rect.x += dx #Left-Right
        self.rect.y += dy #Jump

    def get_coordinates(dx, dy):
        return (dx, dy)
    
player1 = Player(200, 375)
player2 = Player(700, 375)
with open("Player1_Info.data","wb") as file:
    pickle.dump(player1, file) 

