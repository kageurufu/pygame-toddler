import random
import typing

import pygame

from toddler.basic_types import Vec2D


def iter_sequence(seq: typing.List[typing.Any]):
    while True:
        for i in seq:
            yield i


def random_pos_within(screen: pygame.Surface) -> Vec2D:
    return Vec2D(random.randint(0, screen.get_width()), random.randint(0, screen.get_height() / 2))
