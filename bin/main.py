import pygame
import game_functions as gf
from game_screen import GameScreen
from main_menu import Main_menu, Options, Start_menu
from settings import Settings


def run():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height), vsync=1)
    pygame.display.set_caption("PythonMind")
    pygame.display.set_icon(settings.icon)

    main_menu = Main_menu(settings, screen)
    option_menu = Options(settings, screen)
    start_menu = Start_menu(settings, screen)

    game_screen = GameScreen(settings, screen)

    while game_screen.retry is False:
        clockobject = pygame.time.Clock()
        clockobject.tick(60)

        menu_dict = {
            "main_menu": main_menu,
            "option_menu": option_menu,
            "start_menu": start_menu
        }
        if main_menu.active:
            main_menu.update(menu_dict)
        elif option_menu.active:
            option_menu.update(menu_dict)
        elif start_menu.active:
            start_menu.update(menu_dict, game_screen)
        else:
            game_screen.update(menu_dict)

        gf.check_events(settings, screen, menu_dict, game_screen)
        gf.update_screen(settings, screen, menu_dict, game_screen)

    if game_screen.retry == "yes":
        run()


run()
