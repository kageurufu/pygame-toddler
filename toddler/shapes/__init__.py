import random

import pygame

from toddler.drawable import DrawableList
from .shape import Shape
from .circle import Circle
from .polygon import Polygon
from .square import Square
from .star import Star
from .firework import Firework


def random_shape(screen: pygame.Surface, shapes: DrawableList) -> Shape:
    return random.choice([
        Circle,
        Polygon,
        Square,
        Star,
        Firework,
    ]).new_random(screen, shapes)
