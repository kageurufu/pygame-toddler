import pygame

from toddler.fonts import init_fonts
from toddler.mainloop import GameState

pygame.init()
init_fonts()

game_state = GameState()
game_state.loop()
