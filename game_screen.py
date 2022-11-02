import pygame
from button import Button
from guess_area import Guessbox
from game_board import Gameboard
import game_functions as gf

class GameScreen():

    def __init__(self,settings,screen):
        self.settings, self.screen = settings, screen
        self.game_board = Gameboard(settings,screen)
        self.guess_box = Guessbox(settings,screen, self.game_board)
        self.won, self.loss, self.active, self.retry = False,False,False,False
        self.time_string = []

        self.create_button()
        
        #Debug add in x amount of fake guesses
        self.fake_guesses = 6
        #Debug var
        self.x = 0

    def update(self,menu_dict):
        if self.active:
            self.guess_box.update()
            self.game_board.update()
            self.menu_dict = menu_dict

            if not self.won or not self.loss:
                self.update_timer()

            #check to see if the game has been won
            self.won = self.game_board.won
            if self.won and self.x == 0:
                self.do_win()
                self.x = 1

            if len(self.game_board.guess_list) > self.settings.max_guesses - 1:
                self.do_lose()
            if self.fake_guesses != 0:
                self.guess_box.create_fake_guess()
                self.fake_guesses-=1

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
        font = pygame.font.SysFont(None, self.settings.font_size_timer)  # type: ignore
        counting_text = font.render(str(self.time_string), 1, self.settings.hud_colors['red'])  # type: ignore
        counting_rect = counting_text.get_rect(centerx= self.game_board.code.bbox_rect.left /2, centery= self.game_board.code.bbox_rect.centery)
        self.screen.blit(counting_text, counting_rect)

    def create_button(self):
        self.back_button = Button(self.screen,self.settings,"<",(20,self.settings.screen_height - 30),"gs")
        self.back_button.rect.size = (40,60)
        self.back_button.rect.bottomleft = (0,self.settings.screen_height)


    def do_win(self):
        self.win = True
        self.winscreen = Winscreen(self.screen,self.settings)
        
    def do_lose(self):
        self.loss = True
        self.losescreen = Losescreen(self.screen,self.settings)

    def click(self,pos):
        x,y = pos
        try:
            if self.winscreen.retry_button.rect.collidepoint(x,y):
                self.retry = "yes"
        except:
            pass
        try:
            if self.losescreen.retry_button.rect.collidepoint(x,y):
                self.retry = "yes"
        except:
            pass
        
        if self.back_button.rect.collidepoint(x,y):
            self.active = False
            self.menu_dict["start_menu"].active = True
            self.game_board.total_guesses = []


class Winscreen():
    def __init__(self, screen,settings) -> None:
        self.screen, self.settings = screen, settings
        self.darken_surf = gf.get_surf_darken_screen(screen, settings)
        
        center_pos = (self.settings.screen_width/2,self.settings.screen_height/2)
        self.retry_button = Button(self.screen,self.settings,"Retry",center_pos,"gs")
    
    def blitme(self):
        self.screen.blit(self.darken_surf, self.settings.rect)
        self.retry_button.blitme()
    
class Losescreen():
    def __init__(self, screen,settings) -> None:
        self.screen, self.settings = screen, settings
        self.darken_surf = gf.get_surf_darken_screen(screen, settings)
        
        center_pos = (self.settings.screen_width/2,self.settings.screen_height/2)
        self.retry_button = Button(self.screen,self.settings,"Retry",center_pos,"gs")
    
    def blitme(self):
        self.screen.blit(self.darken_surf, self.settings.rect)
        self.retry_button.blitme()