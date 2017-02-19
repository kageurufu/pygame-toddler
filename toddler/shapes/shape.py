from abc import abstractmethod

import pygame

from toddler.drawable import Drawable


class Shape(Drawable):
    age = 0

    @classmethod
    @abstractmethod
    def new_random(cls, screen: pygame.Surface) -> Drawable:
        pass
