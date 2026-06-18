import pygame

from circleshape import CircleShape
from constants import SHOT_COLOR, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS, SHOT_COLOR)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius)

    def update(self, dt: float) -> None:
        self.position -= self.velocity * dt
