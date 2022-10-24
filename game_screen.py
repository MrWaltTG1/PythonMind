import pygame
from button import Button
from guess_area import Guessbox
from game_board import Gameboard
import game_functions as gf

class GameScreen():
    
    def __init__(self,settings,screen):
        self.settings = settings
        self.screen = screen
        self.game_board = Gameboard(settings,screen)
        self.guess_box = Guessbox(settings,screen, self.game_board)
        self.won = False
        self.loss = False
        self.active = False
        self.retry = False
        self.time_string = []
        
        self.create_button()
        
        #Debug var
        self.x = 0
    
    def update(self,menu_dict):
        if self.active:
            self.guess_box.update()
            self.game_board.update()
            self.menu_dict = menu_dict
            
            if not self.won:
                self.update_timer()
                
            #check to see if the game has been won
            self.won = self.game_board.won
            if self.won and self.x == 0:
                self.do_win()
                self.x = 1
            
            if len(self.game_board.guess_list) > self.settings.max_guesses - 1:
                self.loss = True
                self.do_lose()
    
    def create_timer(self, endtime):
        currenttime = pygame.time.get_ticks()
        if endtime:
            self.endtime = int(endtime + currenttime)
        else:
            self.endtime = self.settings.max_time + currenttime
    
    
    def update_timer(self):
        currenttime = pygame.time.get_ticks()
        new_time = self.endtime - currenttime
        
        minutes, seconds, milliseconds = gf.convert_ticks_to_time(new_time)
        
        if new_time >= 0:
            self.time_string = str("%s:%s" % (minutes, seconds))
        else:
            self.loss = True
            self.do_lose()
    
    
    def draw_timer(self):
        font = pygame.font.SysFont(None, 32)  # type: ignore
        counting_text = font.render(str(self.time_string), 1, self.settings.hud_colors['red'])  # type: ignore
        counting_rect = counting_text.get_rect(centerx= self.settings.screen_width / 2)
        self.screen.blit(counting_text, counting_rect)
    
    def create_button(self):
        self.back_button = Button(self.screen,self.settings,"<",(20,self.settings.screen_height - 30),"gs")
        self.back_button.rect.size = (40,60)
        self.back_button.rect.bottomleft = (0,self.settings.screen_height)
        
    
    def do_win(self):
        self.retry_button = Button(self.screen,self.settings,"Retry",(self.settings.screen_width/2,self.settings.screen_height/2),"gs")
    
    def do_lose(self):
        self.retry_button = Button(self.screen,self.settings,"Retry",(self.settings.screen_width/2,self.settings.screen_height/2),"gs")
    
    def click(self,pos):
        x,y = pos
        if self.won or self.loss:
            if self.retry_button.rect.collidepoint(x,y):
                self.retry = "yes"
        if self.back_button.rect.collidepoint(x,y):
            self.active = False
            self.menu_dict["start_menu"].active = True
            self.game_board.total_guesses = []
            
    def blit_darken_screen(self):
        darken_surf = pygame.Surface((self.settings.screen_width, self.settings.screen_height), pygame.SRCALPHA)
        darken_surf.set_alpha(100)
        pygame.draw.rect(darken_surf,(0,0,0),self.settings.rect)
        self.screen.blit(darken_surf,self.settings.rect)