import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x,y, 80, 180))

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    #MOVEMENT
    def move(self):
        SPEED = 10
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        
        #UPDATE POSITION
        self.rect.x += dx #Left-Right
        self.rect.y += dy #Jump

