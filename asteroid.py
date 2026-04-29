import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        points = self.position
        pygame.draw.circle(screen, "white", points, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_kind = old_radius / ASTEROID_MIN_RADIUS
        new_kind = old_kind - 1
        new_radius = new_kind * ASTEROID_MIN_RADIUS
        self.kill()
        if new_kind <= ASTEROID_MIN_RADIUS:
                return
        else:
            log_event("asteroid split")
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity.rotate(random.randint(20, 50))
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity.rotate(random.randint(-20, -50))