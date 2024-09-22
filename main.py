import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    font = pygame.font.SysFont(None, 25)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_filed = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                print(f"Total points: {player.current_points}")
                exit(0)
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    player.add_points()
                    bullet.kill()

        txt = font.render(
            f"Asteroids destroyed: {player.current_points}", True, "white"
        )

        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))
        screen.blit(txt, (20, 20))
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
