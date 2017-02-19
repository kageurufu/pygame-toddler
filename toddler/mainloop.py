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


shapes: DrawableList = []


def mainloop(screen: pygame.Surface):
    running = True
    font16: pygame.font.Font = pygame.font.SysFont('Calibri', 16)
    clock: pygame.time.Clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in string.ascii_letters + string.digits:
                    shapes.append(Letter.new_random(screen, pygame.key.name(event.key)))
                else:
                    shapes.append(random_shape(screen, shapes))

        screen.fill(BLACK)

        for shape in list(shapes):
            if not shape.tick(clock.get_time(), screen):
                shapes.remove(shape)
            else:
                shape.blit(screen)

        screen.blit(font16.render('{:0.1f} fps'.format(clock.get_fps()), False, WHITE), (10, font16.get_height()))
        pygame.display.flip()

    pygame.quit()
