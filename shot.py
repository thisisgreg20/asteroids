import pygame
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