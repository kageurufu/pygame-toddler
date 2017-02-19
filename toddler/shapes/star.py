import math
import random
import typing

import pygame
import pygame.gfxdraw
from pygame.math import Vector2

from toddler.colors import random_color
from toddler.drawable import DrawableList
from toddler.shapes.shape import Shape
from toddler.utils import iter_sequence, random_pos_within


class Star(Shape):
    def __init__(self, pos: Vector2, outer_radius: int, inner_radius: int, points: int, color: pygame.Color):
        max_radius = max(outer_radius, inner_radius)
        surface = pygame.Surface((max_radius * 2, max_radius * 2), pygame.SRCALPHA, 32).convert_alpha()
        pointlist: typing.List[Vector2] = [
            Vector2(outer_radius + math.cos(theta) * radius,
                    outer_radius + math.sin(theta) * radius)
            for theta, radius in zip(map(math.radians, range(0, 360, int(180 / points))),
                                     iter_sequence([inner_radius, outer_radius])
                                     )
            ]
        pygame.gfxdraw.aapolygon(surface, pointlist, color)
        pygame.gfxdraw.filled_polygon(surface, pointlist, color)

        super(Star, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface, shapes: DrawableList):
        return cls(
            random_pos_within(screen),
            random.randint(40, 100),
            random.randint(20, 80),
            random.randint(4, 8),
            random_color()
        )
