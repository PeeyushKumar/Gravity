import pygame

class CustomGroup(pygame.sprite.Group):
    def update_colliding_forces(self):
        for sprite in self.sprites():
            sprite.update_colliding_forces()