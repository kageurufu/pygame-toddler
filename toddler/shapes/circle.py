import random

import pygame
import pygame.gfxdraw
from pygame.math import Vector2

from toddler.colors import random_color
from toddler.drawable import DrawableList
from toddler.shapes.shape import Shape
from toddler.utils import random_pos_within


class Circle(Shape):
    def __init__(self, pos: Vector2, radius: int, color: pygame.Color, width: int = 0):
        surface = pygame.Surface(((radius + width) * 2, (radius + width) * 2), pygame.SRCALPHA, 32).convert_alpha()
        pygame.gfxdraw.aacircle(surface, radius, radius, radius, color)
        pygame.gfxdraw.filled_circle(surface, radius, radius, radius, color)
        super(Circle, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface, shapes: DrawableList) -> Shape:
        return cls(
            random_pos_within(screen),
            random.randint(30, 60),
            random_color()
        )
