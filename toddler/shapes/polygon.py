import math
import typing

import pygame

from toddler.drawable import Drawable
from toddler.basic_types import Vec2D


class Polygon(Drawable):
    def __init__(self, pos: Vec2D, radius: int, points: int, color: pygame.Color):
        surface = pygame.Surface((radius * 2, radius * 2))
        pointlist: typing.List[Vec2D] = [(radius + math.cos(theta) * radius,
                                          radius + math.sin(theta) * radius)
                                         for theta in map(math.radians, range(0, 360, int(360 / points)))
                                         ]
        pygame.draw.polygon(surface, color, pointlist)

        super(Polygon, self).__init__(surface, pos)
