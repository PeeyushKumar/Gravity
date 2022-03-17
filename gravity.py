import pygame, sys

from level import Level
from settings import *

class Gravity:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Gravity')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT \
                    or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
            self.screen.fill('white')
            self.level.update()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    gravity = Gravity()
    gravity.run()