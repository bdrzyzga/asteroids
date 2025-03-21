import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()  # Remove the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid — no split

        # New smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Two new velocity directions (rotated from original)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two new asteroids at the same position
        from asteroid import Asteroid  # prevent circular import at module level
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2

