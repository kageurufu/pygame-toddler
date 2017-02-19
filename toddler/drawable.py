import typing

import pygame

from toddler.basic_types import Vec2D


class Drawable(object):
    surface: pygame.Surface
    pos: pygame.Rect

    def __init__(self, surface: pygame.Surface, pos: Vec2D):
        self.surface = surface
        self.pos = pos

    def blit(self, screen: pygame.Surface):
        screen.blit(self.surface, self.pos)


DrawableList = typing.List[Drawable]
