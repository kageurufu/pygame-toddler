import random
import typing

import pygame.font


def generate_fonts() -> typing.List[pygame.font.Font]:
    fonts = []
    for font_name in ['Calibri']:
        for font_size in range(128, 400, 12):
            fonts.append(pygame.font.SysFont(font_name, font_size))
    return fonts


FONTS = None


def init_fonts():
    global FONTS
    FONTS = generate_fonts()


def random_font() -> pygame.font.Font:
    return random.choice(FONTS)
