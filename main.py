import pygame
import game_functions as gf
from settings import Settings

def run():
    pygame.init()
    settings = Settings()
    
    screen=pygame.display.set_mode((settings.screen_width, settings.screen_height), vsync= 1)
    pygame.display.set_caption("Pirate invasion")
    while True:
        pass

run()