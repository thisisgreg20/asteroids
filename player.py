from circleshape import *
from constants import PLAYER_RADIUS,LINE_WIDTH

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS, LINE_WIDTH)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.pos_list = []
        self.pos_list.append((self.x + self.y))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, pos_list, LINE_WIDTH):
        self.__init__(screen, pos_list, LINE_WIDTH)
        pygame.draw.polygon(screen, "white", pos_list, LINE_WIDTH)

    def update(self, dt):
        # must override
        pass