import pygame
from button import Button
from guess_area import Guessbox
from game_board import Gameboard
import game_functions as gf


class GameScreen():

    def __init__(self, settings, screen):
        self.settings, self.screen = settings, screen
        self.game_board = Gameboard(settings, screen)
        self.guess_box = Guessbox(settings, screen, self.game_board)
        self.won, self.loss, self.active, self.retry = False, False, False, False
        self.time_string = []

        self.create_button()

        # Debug add in x amount of fake guesses
        self.fake_guesses = 0
        # Debug var
        self.x = 0

    def update(self, menu_dict):
        if self.active:
            self.guess_box.update()
            self.game_board.update()
            self.menu_dict = menu_dict

            if self.won is False and self.loss is False:
                self.update_timer()

            # check to see if the game has been won
            self.won = self.game_board.won
            if self.won and self.x == 0:
                self.do_win()
                self.x = 1

            if len(self.game_board.guess_list) > self.settings.max_guesses - 1:
                self.do_lose()
            if self.fake_guesses != 0:
                self.guess_box.create_fake_guess()
                self.fake_guesses -= 1

    def create_timer(self, endtime):
        currenttime = pygame.time.get_ticks()
        if endtime:
            self.endtime = int(endtime + currenttime)
        else:
            self.endtime = self.settings.max_time + currenttime

    def update_timer(self):
        currenttime = pygame.time.get_ticks()
        new_time = self.endtime - currenttime

        minutes, seconds = gf.convert_ticks_to_time(new_time)

        if new_time >= 0:
            self.time_string = str("%s:%s" % (minutes, seconds))
        else:
            self.do_lose()

    def draw_timer(self):
        font = pygame.font.SysFont(
            None, self.settings.font_size_timer)  # type: ignore
        counting_text = font.render(
            str(self.time_string), 1, self.settings.hud_colors['red'])  # type: ignore
        counting_rect = counting_text.get_rect(
            centerx=self.game_board.code.bbox_rect.left / 2, centery=self.game_board.code.bbox_rect.centery)
        self.screen.blit(counting_text, counting_rect)

    def create_button(self):
        self.back_button = Button(
            self.screen, self.settings, "<", (20, self.settings.screen_height - 30), "gs")
        self.back_button.rect.size = (40, 60)
        self.back_button.rect.bottomleft = (0, self.settings.screen_height)

    def do_win(self):
        self.win = True
        self.winscreen = Winscreen(
            self.screen, self.settings, len(self.game_board.total_guesses))

    def do_lose(self):
        self.loss = True
        self.losescreen = Losescreen(self.screen, self.settings)

    def click(self, pos):
        x, y = pos
        try:
            if self.winscreen.retry_button.rect.collidepoint(x, y):
                self.retry = "yes"

        except:
            pass
        try:
            if self.losescreen.retry_button.rect.collidepoint(x, y):
                self.retry = "yes"

        except:
            pass

        try:
            if self.back_button.rect.collidepoint(x, y):
                self.confirm_popup()
                self.confirm = True
            elif self.confirm_button.rect.collidepoint(x, y):
                self.confirm, self.active = False, False
                self.menu_dict["start_menu"].active = True
                self.game_board.total_guesses, self.game_board.guess_list = [], []
                self.game_board.index, self.game_board.starting_index, self.game_board.ending_index = 0, 0, 6
            elif self.cancel_button.rect.collidepoint(x, y):
                self.confirm = False
        except:
            pass

    def confirm_popup(self):
        self.dark_surf = gf.get_surf_darken_screen(self.screen, self.settings)
        pos1 = self.settings.rect.centerx, self.settings.rect.centery - 40
        pos2 = self.settings.rect.centerx, self.settings.rect.centery + 40
        pos3 = self.settings.rect.centerx, self.settings.rect.centery - 180
        self.confirm_button = Button(
            self.screen, self.settings, "Confirm", pos1, "mm")
        self.cancel_button = Button(
            self.screen, self.settings, "Cancel", pos2, "mm")

        size = (400, 60)
        text = "Are you sure?"
        textbox_list = gf.create_text_box(self.settings, pos3, size, text)
        self.textbox = textbox_list[0]
        self.image = textbox_list[1][0]
        self.image_rect = textbox_list[1][1]


class Winscreen():
    def __init__(self, screen, settings, guesses) -> None:
        self.screen, self.settings = screen, settings
        self.darken_surf = gf.get_surf_darken_screen(screen, settings)

        center_pos = (self.settings.screen_width/2,
                      self.settings.screen_height/2)
        self.retry_button = Button(
            self.screen, self.settings, "Retry", center_pos, "gs")

        pos = (self.settings.rect.centerx, self.settings.rect.centery - 100)
        size = (200, 30)
        text = f"your score is: {settings.max_guesses - guesses}"
        self.textbox_list1 = gf.create_text_box(
            settings, pos, size, text, text_color=self.settings.hud_colors["white"], font_size=50)

        pos = (self.settings.rect.centerx, self.settings.rect.centery - 150)
        text = "Congratulations, you've succesfully guessed the code!"
        self.textbox_list2 = gf.create_text_box(
            settings, pos, size, text, text_color=self.settings.hud_colors["white"], font_size=50)

    def blitme(self):
        self.screen.blit(self.darken_surf, self.settings.rect)
        self.retry_button.blitme()
        self.screen.blit(self.textbox_list1[1][0], self.textbox_list1[1][1])
        self.screen.blit(self.textbox_list2[1][0], self.textbox_list2[1][1])


class Losescreen():
    def __init__(self, screen, settings) -> None:
        self.screen, self.settings = screen, settings
        self.darken_surf = gf.get_surf_darken_screen(screen, settings)

        center_pos = (self.settings.screen_width/2,
                      self.settings.screen_height/2)
        self.retry_button = Button(
            self.screen, self.settings, "Retry", center_pos, "gs")

        pos = (self.settings.rect.centerx, self.settings.rect.centery - 150)
        size = (200, 30)
        text = "You've failed to crack the code"
        self.textbox_list1 = gf.create_text_box(
            settings, pos, size, text, text_color=self.settings.hud_colors["white"], font_size=50)

    def blitme(self):
        self.screen.blit(self.darken_surf, self.settings.rect)
        self.retry_button.blitme()
        self.screen.blit(self.textbox_list1[1][0], self.textbox_list1[1][1])
