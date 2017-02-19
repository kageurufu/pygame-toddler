import random

import pygame
from pygame.math import Vector2

from toddler.drawable import DrawableList
from toddler.shapes import Circle
from toddler.shapes import Shape


class Firework(Circle):
    _shapes: DrawableList

    def __init__(self, pos: Vector2, radius: int, color: pygame.Color, width: int = 0):
        super().__init__(pos, radius, color, width)
        self.color = color
        self.fuse = random.randint(200, 1000)

    def tick(self, t: int, screen):
        self.fuse -= t
        if self.fuse <= 0:
            self.explode()
            return False
        return True

    def explode(self):
        for _ in range(random.randint(25, 50)):  # Up to 50 particles
            particle = Circle(self.pos, random.randint(3, 10), self.color)
            particle.delta = Vector2(random.random() * 40 - 20, random.random() * 40 - 30)
            self._shapes.append(particle)

    @classmethod
    def new_random(cls, screen: pygame.Surface, shapes: DrawableList) -> Shape:
        firework = super(Firework, cls).new_random(screen, shapes)
        firework._shapes = shapes
        return firework
