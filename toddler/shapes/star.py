import math
import typing

import pygame

from toddler.drawable import Drawable
from toddler.basic_types import Vec2D
from toddler.utils import iter_sequence


class Star(Drawable):
    def __init__(self, pos: Vec2D, outer_radius: int, inner_radius: int, points: int, color: pygame.Color):
        surface = pygame.Surface((outer_radius * 2, outer_radius * 2))
        pointlist: typing.List[Vec2D] = [(radius + math.cos(theta) * radius,
                                          radius + math.sin(theta) * radius)
                                         for theta, radius in
                                         zip(map(math.radians, range(0, 360, int(180 / points))),
                                             iter_sequence([inner_radius, outer_radius]))
                                         ]
        pygame.draw.polygon(surface, color, pointlist)

        super(Star, self).__init__(surface, pos)
