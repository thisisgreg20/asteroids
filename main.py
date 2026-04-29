import pygame
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
### Groups ###
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)
    Shot.containers = (drawable, shots, updatable)
### ###### ###

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(FPS_CAP) / 1000
        screen.fill("black")
        updatable.update(dt)
        
        for other in asteroids:
            player.collides_with(other)
        
        for asteroid in asteroids:
            for shot in shots:
                shot.shot_hits(asteroid)
        
        for sprites in drawable:
            sprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()