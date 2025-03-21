import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    CircleShape.containers = updatables, drawables
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.display.set_caption("Asteroids")

    # Initialize clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        screen.fill("black")
        for sprite in drawables:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()
