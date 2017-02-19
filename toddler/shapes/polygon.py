import math
import typing

import pygame
import pygame.gfxdraw
import random

from pygame.math import Vector2

from toddler.colors import random_color
from toddler.drawable import DrawableList
from toddler.shapes.shape import Shape
from toddler.utils import random_pos_within


class Polygon(Shape):
    def __init__(self, pos: Vector2, radius: int, points: int, color: pygame.Color):
        surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA, 32).convert_alpha()
        pointlist: typing.List[Vector2] = [Vector2(radius + math.cos(theta) * radius,
                                                   radius + math.sin(theta) * radius)
                                           for theta in map(math.radians, range(0, 360, int(360 / points)))
                                           ]
        pygame.gfxdraw.aapolygon(surface, pointlist, color)
        pygame.gfxdraw.filled_polygon(surface, pointlist, color)

        super(Polygon, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface, shapes: DrawableList) -> Shape:
        return cls(
            random_pos_within(screen),
            random.randint(40, 100),
            random.randint(5, 12),
            random_color()
        )
