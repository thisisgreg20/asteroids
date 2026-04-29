import pygame
from logger import log_event
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        points = self.position
        pygame.draw.circle(screen, "white", points, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def shot_hits(self, other):
        r1 = self.radius
        r2 = other.radius
        p1 = self.position
        p2 = other.position
        distance = pygame.math.Vector2.distance_to(p1, p2)
        check = distance <= (r1 + r2)
        if check == True:
            log_event("asteroid_shot")
            # call asteroid.spawn() here
            pygame.sprite.Sprite.kill(self)
            pygame.sprite.Sprite.kill(other)
        return check