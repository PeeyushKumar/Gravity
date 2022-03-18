import pygame, random

from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, groups, collision_sprites) -> None:
        super().__init__(groups)

        self.position = pygame.Vector2(random.randint(radius, WIDTH-radius), random.randint(radius, HEIGHT-radius))
        self.speed = pygame.Vector2((random.random()-0.5)*10, (random.random()-0.5)*10)
        self.color = random.choice(COLORS)
        self.radius = radius

        self.collision_sprites = collision_sprites
        self.colliding_force = pygame.Vector2(0, 0)
        
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill('white')
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect(center = self.position)
        
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

    
    def update(self) -> None: 

        self.speed += ACCELERATION_DUE_TO_GRAVITY

        self.speed += self.colliding_force
        self.colliding_force *= 0

        if self.rect.left <= 0:
            self.speed.x = abs(self.speed.x)
        
        if self.rect.right >= WIDTH:
            self.speed.x = -abs(self.speed.x)
    
        if self.rect.bottom > HEIGHT and self.speed.y > 0:
            self.speed.y = -abs(self.speed.y)
            self.speed += ACCELERATION_DUE_TO_GRAVITY
            
        self.position += self.speed
        self.rect.center = self.position


    def update_colliding_forces(self) -> None:

        for sprite in self.collision_sprites:
                if self.collides_with(sprite):
                    self.resolve_collision(sprite)


    def collides_with(self, other) -> bool:

        return other is not self \
            and (self.position - other.position).magnitude() <= other.radius + self.radius - ALLOWED_OVERLAP_OFFSET


    def resolve_collision(self, other) -> None:

        direction = (other.position  - self.position).normalize()

        self.colliding_force += -direction * self.speed.dot(direction)
        other.colliding_force += direction * self.speed.dot(direction)
