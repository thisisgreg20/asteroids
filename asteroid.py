import pygame
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