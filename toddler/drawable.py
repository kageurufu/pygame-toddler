import typing

import pygame
from pygame.math import Vector2


class Drawable(object):
    surface: pygame.Surface
    pos: pygame.Rect

    def __init__(self, surface: pygame.Surface, pos: Vector2):
        self.surface = surface
        self.pos = Vector2(pos)

    def tick(self, t: int, screen) -> bool:
        return True

    def blit(self, screen: pygame.Surface):
        screen.blit(self.surface, self.pos)


DrawableList = typing.List[Drawable]
