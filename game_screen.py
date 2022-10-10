import pygame
from datetime import datetime
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
            
            self.update_timer()
            
            #check to see if the game has been won
            self.won = self.game_board.won
            if self.won and self.x == 0:
                print("DING DING DING")
                self.x = 1
            
    def create_timer(self):
        currenttime = pygame.time.get_ticks()
        self.endtime = self.settings.max_time + currenttime
        
    
    def update_timer(self):
        currenttime = pygame.time.get_ticks()
        new_time = self.endtime - currenttime
        
        minutes, seconds, milliseconds = gf.convert_ticks_to_time(new_time)
        
        if new_time >= 0:
            self.time_string = str("%s:%s:%s" % (minutes, seconds, milliseconds))
            
        
    def draw_timer(self):
        font = pygame.font.SysFont(None, 32)
        counting_text = font.render(str(self.time_string), 1, (200,20,0))
        counting_rect = counting_text.get_rect()
        self.screen.blit(counting_text, counting_rect)