import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    print(f"Starting Asteroids with pygame version: {str(pygame.version.ver)}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock() # Initialize the clock before the game opens
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        updatable.update(dt)
        

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()

            if player.collides_with(asteroid) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        


        screen.fill((0,0,0))
        for dra in drawable:
            dra.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Updates the delta value that then gets printed 




if __name__ == "__main__":
    main()
