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
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        random_angle = random.uniform(20, 50) # Random Angle for asteroid1
        new_vel1 = self.velocity.rotate(random_angle)
        random_angle = random.uniform(20, 50) # Random Angle for asteroid2
        new_vel2 = self.velocity.rotate(-random_angle)
        asteroid1.velocity = new_vel1 * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        asteroid2.velocity = new_vel2 * ASTEROID_SPLIT_VELOCITY_MULTIPLIER