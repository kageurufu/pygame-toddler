import random

from .shape import Shape
from .circle import Circle
from .polygon import Polygon
from .square import Square
from .star import Star


def random_shape(screen) -> Shape:
    return random.choice([
        Circle,
        Polygon,
        Square,
        Star
    ]).new_random(screen)
