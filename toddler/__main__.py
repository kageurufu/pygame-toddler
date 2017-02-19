import pygame

from toddler.mainloop import mainloop

pygame.init()

screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)

mainloop(screen)
