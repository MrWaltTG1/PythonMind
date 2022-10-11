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
        self.active = False
        self.time_string = []
        
        #Debug var
        self.x = 0
        
    def update(self):
        if self.active:
            self.guess_box.update()
            self.game_board.update()
            
            if not self.won:
                self.update_timer()
            
            #check to see if the game has been won
            self.won = self.game_board.won
            if self.won and self.x == 0:
                self.do_win()
                self.x = 1
            
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
            print("rip bozo")
            
        
    def draw_timer(self):
        font = pygame.font.SysFont(None, 32)  # type: ignore
        counting_text = font.render(str(self.time_string), 1, (200,20,0))  # type: ignore
        counting_rect = counting_text.get_rect(centerx= self.settings.screen_width / 2)
        self.screen.blit(counting_text, counting_rect)
    
    def do_win(self):
        self.retry_button = Button(self.screen,self.settings,"Retry",(self.settings.screen_width/2,self.settings.screen_height/2),"gs")
        