import pygame
import string

import random

from toddler.basic_types import Vec2D
from toddler.colors import random_color
from toddler.fonts import random_font
from toddler.shapes import Shape
from toddler.utils import random_pos_within


class Letter(Shape):
    def __init__(self, pos: Vec2D, letter: str, font: pygame.font.Font, color: pygame.Color):
        surface = font.render(letter, True, color)
        super(Letter, self).__init__(surface, pos)

    @classmethod
    def new_random(cls, screen: pygame.Surface, letter: str = None) -> Shape:
        return cls(random_pos_within(screen),
                   letter or random.choice(string.ascii_letters),
                   random_font(),
                   random_color())
