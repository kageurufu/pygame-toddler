import pygame

from toddler.mainloop import mainloop
from toddler.fonts import init_fonts

pygame.init()
init_fonts()

screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE, 32)

mainloop(screen)
