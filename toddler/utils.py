import random
import typing

import pygame
from pygame.math import Vector2


def iter_sequence(seq: typing.List[typing.Any]):
    while True:
        for i in seq:
            yield i


def random_pos_within(screen: pygame.Surface) -> Vector2:
    return Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height() / 2))
