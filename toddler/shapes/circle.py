import random

import pygame
import pygame.gfxdraw

from toddler.basic_types import Vec2D
from toddler.colors import random_color
from toddler.shapes.shape import Shape
from toddler.utils import random_pos_within


class Circle(Shape):
    def __init__(self, pos: Vec2D, radius: int, color: pygame.Color, width: int = 0):
        surface = pygame.Surface(((radius + width) * 2, (radius + width) * 2), pygame.SRCALPHA, 32).convert_alpha()
        pygame.gfxdraw.aacircle(surface, radius, radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, radius, radius, radius, color)
        super(Circle, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface) -> Shape:
        return cls(
            random_pos_within(screen),
            random.randint(30, 60),
            random_color()
        )
