import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        r1 = self.radius
        r2 = other.radius
        p1 = self.position
        p2 = other.position
        distance = pygame.math.Vector2.distance_to(p1, p2)
        check = distance <= (r1 + r2)
        if check == True:
            print(f"Alert! Collision Detected P: {p1} A: {p2}")
        return distance <= (r1 + r2)
