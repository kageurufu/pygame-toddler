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
from pygame.math import Vector2

from toddler.colors import BLACK, WHITE
from toddler.drawable import DrawableList
from toddler.shapes import Firework
from toddler.shapes import random_shape
from toddler.shapes.letter import Letter


class GameMode(Enum):
    ATTRACT = 1
    ACTIVE = 2


class GameState(object):
    screen: pygame.Surface
    clock: pygame.time.Clock
    font16: pygame.font.Font
    drawables: DrawableList
    running: bool
    desired_framerate: int = 60
    game_mode: GameMode
    last_keypress: int = 0
    last_generate: int = 0

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE, 32)
        self.drawables = []
        self.running = True
        self.clock = pygame.time.Clock()
        self.font16 = pygame.font.SysFont('Calibri', 16)

        self.game_mode = GameMode.ATTRACT

    def events(self):
        handled_event = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in string.ascii_letters + string.digits:
                    self.drawables.append(Letter.new_random(self.screen, self.drawables, pygame.key.name(event.key)))
                else:
                    self.drawables.append(random_shape(self.screen, self.drawables))
                handled_event = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                firework = Firework.new_random(self.screen, self.drawables)
                firework.pos = Vector2(pygame.mouse.get_pos()) - (Vector2(firework.surface.get_size()) / 2)
                self.drawables.append(firework)
                handled_event = True
        if handled_event and self.game_mode == GameMode.ATTRACT:
            self.game_mode = GameMode.ACTIVE
            self.last_keypress = 0

    def tick(self):
        t = self.clock.get_time()
        self.last_keypress += t

        if self.last_keypress > 5 * 1000:
            self.game_mode = GameMode.ATTRACT

        if self.game_mode == GameMode.ATTRACT:
            self.last_generate += t
            if self.last_generate > 500:
                self.drawables.append(Firework.new_random(self.screen, self.drawables))
                self.last_generate = 0

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
            self.draw_fps()
            self.draw_flip()

        pygame.quit()
