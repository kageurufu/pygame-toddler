import math
import random
import typing

import pygame
import pygame.color

from toddler.utils import iter_sequence

BLACK = pygame.color.Color('black')
WHITE = pygame.color.Color('white')

"""
function makeColorGradient(frequency1, frequency2, frequency3,
                             phase1, phase2, phase3,
                             center, width, len)
  {
    if (center == undefined)   center = 128;
    if (width == undefined)    width = 127;
    if (len == undefined)      len = 50;

    for (var i = 0; i < len; ++i)
    {
       var red = Math.sin(frequency1*i + phase1) * width + center;
       var grn = Math.sin(frequency2*i + phase2) * width + center;
       var blu = Math.sin(frequency3*i + phase3) * width + center;
       document.write( '<font color="' + RGB2Color(red,grn,blu) + '">&#9608;</font>');
    }
  }
"""


def generate_color_gradient(f1: float, f2: float, f3: float,
                            p1: int, p2: int, p3: int,
                            center=128, width=127, count=50) -> typing.List[pygame.Color]:
    colors = []
    for i in range(0, count):
        colors.append(
            pygame.Color(
                int(math.sin(f1 * i + p1) * width + center),
                int(math.sin(f2 * i + p2) * width + center),
                int(math.sin(f3 * i + p3) * width + center),
                255
            )
        )
    return colors


COLORS = generate_color_gradient(.3, .3, .3, 0, 2, 4)

seq = iter_sequence(COLORS)


def random_color() -> pygame.Color:
    return random.choice(COLORS)
