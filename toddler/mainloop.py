from enum import Enum

import pygame
import pygame.color
import pygame.constants
import pygame.display
import pygame.event
import pygame.font
import pygame.surface
import pygame.time
import string

from toddler.colors import BLACK, WHITE, random_color
from toddler.drawable import DrawableList
from toddler.fonts import random_font
from toddler.shapes import Circle, Polygon, Square, Star, random_shape
from toddler.shapes.letter import Letter


class Mode(Enum):
    ATTRACT = 1
    PLAY = 2


def mainloop(screen: pygame.Surface):
    running = True
    font16: pygame.font.Font = pygame.font.SysFont('Calibri', 16)
    clock: pygame.time.Clock = pygame.time.Clock()

    shapes: DrawableList = []

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in string.ascii_letters + string.digits:
                    shapes.append(Letter.new_random(screen, pygame.key.name(event.key)))
                else:
                    shapes.append(random_shape(screen))

        screen.fill(BLACK)

        # Start
        # Physics
        for shape in list(shapes):
            if not shape.tick(clock.get_time(), screen):
                print('Removing {!r}'.format(shape))
                shapes.remove(shape)

        for shape in shapes:
            shape.blit(screen)

        # End

        screen.blit(font16.render('{:0.1f} fps'.format(clock.get_fps()), False, WHITE), (10, font16.get_height()))
        pygame.display.flip()

    pygame.quit()
