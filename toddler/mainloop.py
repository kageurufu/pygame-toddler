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
from toddler.shapes.circle import Circle
from toddler.shapes.polygon import Polygon
from toddler.shapes.square import Square
from toddler.shapes.star import Star


def mainloop(screen: pygame.Surface):
    running = True
    keys_pressed = set()
    font16: pygame.font.Font = pygame.font.SysFont('Calibri', 16)
    # font24: pygame.font.Font = pygame.font.SysFont('Calibri', 24)
    clock: pygame.time.Clock = pygame.time.Clock()

    shapes: DrawableList = [
        Circle((100, 100), 50, pygame.Color('blue')),
        Square((100, 200), 50, pygame.Color('red')),
        Polygon((100, 300), 50, 6, pygame.Color('green')),
        Star((100, 400), 50, 40, 5, pygame.Color('purple')),
    ]

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
            if event.type == pygame.KEYUP:
                keys_pressed.remove(event.key)

        screen.fill(BLACK)

        # Start

        for shape in shapes:
            shape.blit(screen)

        # End

        screen.blit(font16.render('{:0.1f} fps'.format(clock.get_fps()), False, WHITE), (10, font16.get_height()))
        screen.blit(font16.render(repr(keys_pressed), False, WHITE), (10, font16.get_height() * 2))
        pygame.display.flip()

    pygame.quit()
