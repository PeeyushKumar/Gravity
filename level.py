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

    def collider(self) -> None:
        for sprite1 in self.collision_sprites:
            for sprite2 in self.collision_sprites:
                
                if sprite1.collides_with(sprite2):
                    sprite1.resolve_collision(sprite2)


    def update(self) -> None:

        self.collider()

        for ball in self.balls:
            ball.update()

        self.visible_sprites.draw(self.screen)