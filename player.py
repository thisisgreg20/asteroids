import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shot_gcd = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: # Move forward
            self.move(dt)
        if keys[pygame.K_a]: # Rotate left / counter-clockwise
            self.rotate(dt * -1)
        if keys[pygame.K_s]: # Move backwards
            self.move(dt * -1)
        if keys[pygame.K_d]: # Rotate right / clockwise
            self.rotate(dt)
        if keys[pygame.K_SPACE]: # Shoot
            self.shoot()
        if keys[pygame.K_r]: # Reset player position
            self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        self.shot_gcd -= dt

    def shoot(self):
        if self.shot_gcd > 0: # Limits shots cooldown
            return
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity = rotated_with_speed_vector
        self.shot_gcd = PLAYER_SHOOT_COOLDOWN_SECONDS
        