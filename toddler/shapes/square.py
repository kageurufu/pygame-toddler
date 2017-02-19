import pygame

from toddler.drawable import Drawable
from toddler.basic_types import Vec2D


class Square(Drawable):
    def __init__(self, pos: Vec2D, size: int, color: pygame.Color):
        surface = pygame.Surface((size, size))
        surface.fill(color)
        super(Square, self).__init__(surface, pos)
