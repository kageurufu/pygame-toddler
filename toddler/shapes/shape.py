from abc import abstractmethod

import pygame
from pygame.math import Vector2

from toddler.constants import TERMINAL_VELOCITY, ACCELERATION
from toddler.drawable import Drawable, DrawableList


class Shape(Drawable):
    delta: Vector2

    def __init__(self, surface: pygame.Surface, pos: Vector2):
        super().__init__(surface, pos)
        self.age = 0
        self.delta = Vector2(0, 0)

    @classmethod
    @abstractmethod
    def new_random(cls, screen: pygame.Surface, shapes: DrawableList) -> Drawable:
        pass

    def tick(self, t: int, screen):
        self.age += t
        self.delta = self.delta.lerp(TERMINAL_VELOCITY, ACCELERATION / t)
        self.pos += self.delta
        return self.pos.y < screen.get_height()
