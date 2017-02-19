import string
from enum import Enum

import pygame
import pygame.color
import pygame.constants
import pygame.display
import pygame.event
import pygame.font
import pygame.surface
import pygame.time

from toddler.colors import BLACK, WHITE
from toddler.drawable import DrawableList
from toddler.shapes import random_shape
from toddler.shapes.letter import Letter


class Mode(Enum):
    ATTRACT = 1
    PLAY = 2


class GameState(object):
    screen: pygame.Surface
    clock: pygame.time.Clock
    font16: pygame.font.Font
    drawables: DrawableList
    running: bool
    desired_framerate: int = 60

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE, 32)
        self.drawables = []
        self.running = True
        self.clock = pygame.time.Clock()
        self.font16 = pygame.font.SysFont('Calibri', 16)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in string.ascii_letters + string.digits:
                    self.drawables.append(Letter.new_random(self.screen, pygame.key.name(event.key)))
                else:
                    self.drawables.append(random_shape(self.screen, self.drawables))

    def tick(self):
        t = self.clock.get_time()
        for drawable in list(self.drawables):
            if not drawable.tick(t, self.screen):
                self.drawables.remove(drawable)

    def blit(self):
        for drawable in self.drawables:
            drawable.blit(self.screen)

    def draw_start(self):
        self.screen.fill(BLACK)

    def draw_fps(self):
        self.screen.blit(
            self.font16.render('{:0.1f} fps'.format(self.clock.get_fps()), False, WHITE),
            (10, self.font16.get_height()))

    def draw_flip(self):
        pygame.display.flip()

    def loop(self):
        while self.running:
            self.clock.tick(self.desired_framerate)
            self.events()
            self.tick()
            self.draw_start()
            self.blit()
            self.draw_flip()

        pygame.quit()
