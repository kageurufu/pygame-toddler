import typing

import pygame

from toddler.basic_types import Vec2D


class Drawable(object):
    surface: pygame.Surface
    pos: pygame.Rect
    age: int

    def __init__(self, surface: pygame.Surface, pos: Vec2D):
        self.surface = surface
        self.pos = Vec2D(*pos)
        self.age = 0

    def tick(self, t: int, screen):
        self.age += t
        self.pos = Vec2D(self.pos.x, self.pos.y + t / 2)
        return self.pos.y < screen.get_height()

    def blit(self, screen: pygame.Surface):
        screen.blit(self.surface, self.pos)


DrawableList = typing.List[Drawable]
