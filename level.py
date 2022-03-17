import pygame

from ball import Ball
from settings import *

class Level:
    def __init__(self) -> None:
        
        self.screen = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.balls = []

        for _ in range(AMOUNT):
            ball = Ball(RADIUS, [self.visible_sprites, self.collision_sprites], self.collision_sprites)
            self.balls.append(ball)        


    def update(self) -> None:

        for ball in self.balls:	
            ball.update()

        self.visible_sprites.draw(self.screen)