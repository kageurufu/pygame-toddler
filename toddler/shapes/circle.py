import pygame

from toddler.drawable import Drawable
from toddler.basic_types import Vec2D


class Circle(Drawable):
    def __init__(self, pos: Vec2D, radius: int, color: pygame.Color, width: int = 0):
        surface = pygame.Surface(((radius + width) * 2, (radius + width) * 2))
        pygame.draw.circle(surface, color, (radius + width, radius + width), radius, width)
        super(Circle, self).__init__(surface, pos)
