import random

import pygame

from toddler.basic_types import Vec2D
from toddler.colors import random_color
from toddler.shapes.shape import Shape
from toddler.utils import random_pos_within


class Square(Shape):
    def __init__(self, pos: Vec2D, size: int, color: pygame.Color):
        surface = pygame.Surface((size, size))
        surface.fill(color)
        super(Square, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface) -> Shape:
        return cls(
            random_pos_within(screen),
            random.randint(40, 120),
            random_color()
        )
