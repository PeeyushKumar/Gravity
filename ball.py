import pygame, random

from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, groups, collision_sprites) -> None:
        super().__init__(groups)

        self.position = pygame.Vector2(random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius))
        self.speed = pygame.Vector2((random.random()-0.5)*10, (random.random()-0.5)*10)
        self.color = random.choice(COLORS)
        self.radius = radius
        
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill('white')
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect(center = self.position)
        
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

        self.collision_sprites = collision_sprites
    
    def update(self) -> None: 

        self.speed += ACCELERATION_DUE_TO_GRAVITY

        for sprite in self.collision_sprites:
            if self.collidesWith(sprite):
                self.resolveCollision(sprite)


        if self.rect.left <= 0:
            self.speed.x = abs(self.speed.x)
        
        if self.rect.right >= WIDTH:
            self.speed.x = -abs(self.speed.x)
    
        if self.rect.bottom > HEIGHT and self.speed.y > 0:
            self.speed.y = -abs(self.speed.y)
            self.speed += ACCELERATION_DUE_TO_GRAVITY
            
        self.position += self.speed
        self.rect.center = self.position

            
    def collidesWith(self, other) -> bool:

        pos_self = self.position
        pos_other = other.position

        return other is not self and (pos_self - pos_other).magnitude() <= other.radius+self.radius-ALLOWED_OVERLAP_OFFSET

    def resolveCollision(self, other) -> None:

        direction = self.position - other.position
        direction = direction.normalize()

        force_on_self = direction * other.speed.magnitude()
        force_on_other = direction * -1 * self.speed.magnitude()

        self.speed += force_on_self * 0.4
        other.speed += force_on_other * 0.4
