import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_COLORS, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, color: str) -> None:
        super().__init__(x, y, radius, color)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            self.color,
            self.position,
            self.radius,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (kind := self.radius // ASTEROID_MIN_RADIUS) == 1:
            return

        kind -= 1

        log_event("asteroid_split")

        angle = random.uniform(20, 5)
        new_radius = kind * ASTEROID_MIN_RADIUS
        color = ASTEROID_COLORS[-kind]

        asteroid1 = Asteroid(*self.position, new_radius, color)
        asteroid2 = Asteroid(*self.position, new_radius, color)

        asteroid1.velocity = 1.2 * self.velocity.rotate(angle)
        asteroid2.velocity = 1.2 * self.velocity.rotate(-angle)
