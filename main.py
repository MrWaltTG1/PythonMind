import pygame
import game_functions as gf
from settings import Settings
from main_menu import Main_menu, Options


def run():
    pygame.init()
    settings = Settings()
    
    
    
    screen=pygame.display.set_mode((settings.screen_width, settings.screen_height), vsync= 1)
    pygame.display.set_caption("PythonMind")
    
    main_menu = Main_menu(settings, screen)
    option_menu = Options(settings, screen)
    while True:        
        clockobject = pygame.time.Clock()
        clockobject.tick(60)
        
        menu_list = [main_menu, option_menu]
        if main_menu.active:
            main_menu.update(menu_list)
        elif option_menu.active:
            option_menu.update(menu_list)
        
        gf.check_events(settings, screen, main_menu, option_menu)
        gf.update_screen(settings, screen, main_menu, option_menu)
            

run()