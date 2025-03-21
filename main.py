import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.display.set_caption("Asteroids")

    # Initialize clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")        # Clear screen
        player.draw(screen)         # Draw player triangle
        pygame.display.flip()       # Update screen
        dt = clock.tick(60) / 1000  # Frame limiter
        player.update(dt)           # Update player


if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()
