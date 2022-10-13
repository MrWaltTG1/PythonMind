import random
import pygame
import collections
from secret_code import SecretCode

class Gameboard():
    def __init__(self, settings,screen) -> None:
        self.screen = screen
        self.settings = settings
        
        self.pos = (settings.screen_width / 2, settings.screen_height / 2) #Top left position
        self.width = settings.screen_width * 0.9
        self.height = settings.screen_height * 0.85
        self.color = (92, 64, 51)
        
        self.rect = pygame.Rect(self.pos, (self.width,self.height))
        self.rect.center = self.pos
        self.rect.top += 60
        self.new_guess = False
        self.guess_list = []
        self.total_guesses = []
        self.index = 0
        self.won = False
        self.create_secret_code()
        self.secret_code = self.code.pin_list
        
    def update(self):
        if self.new_guess:
            for guess in self.total_guesses:
                guess.bbox.midtop = guess.bbox.midbottom
            self.create_guess()
            self.new_guess = False
        self.code.update(self.won)

        #UPDATE the new guess positions
        for guess in self.total_guesses:
            if guess.won == True:
                self.won = True
        
    def create_guess(self):
        if self.guess_list:
            if len(self.guess_list) > 0:
                self.guess_list[self.index]["pos"] = (0,0)
                add_guess = Guess(self.settings,self.screen,self.guess_list[self.index]["pos"],self.guess_list[self.index]["colors"])
                add_guess.bbox.midtop = self.rect.midtop
                add_guess.get_results(self.secret_code)
                self.total_guesses.append(add_guess)
                self.index += 1
    
    def create_secret_code(self):
        self.code = SecretCode(self.settings,self.screen)
    
    def blitme(self): 
        pygame.draw.rect(self.screen,self.color,self.rect, 5)
        self.code.blitme()
        
        
class Guess():
    def __init__(self, settings,screen, pos, colors) -> None:
        self.screen = screen
        self.settings = settings
        self.won = False
        self.colors = colors
        self.pos = pos
        self.width, self.height = (settings.screen_width * 0.9) - 10, 100
        
        self.bbox = pygame.Rect(pos,(self.width,self.height))
        self.bbox.midtop = pos
        self.color = (51,120,59)
    
    def draw_pins(self):
        pos = (self.bbox.midleft[0]  + self.settings.guess_pin_radius * 2 + 20, self.bbox.midleft[1])
        for color in self.colors:
            pygame.draw.circle(self.screen,color,pos,self.settings.guess_pin_radius)
            pos = (pos[0] + self.settings.guess_pin_radius * 2 + 20, self.bbox.midleft[1])
    
    def get_results(self, secret_code):
        self.result_type_list = ["full", "half", "none"]
        self.result_list = []
        for code in secret_code:
            print(code.color)
        
        self.result_list = []
        code_color_list = []
        guess_color_list = []
        for code in secret_code:
            code_color_list.append(code.color)
        for color in self.colors:
            guess_color_list.append(color)
        
        i = 3
        #GET FULL ONES
        while i > -1:
            if code_color_list[i] == guess_color_list[i]:
                self.result_list.append("full")
                code_color_list.pop(i)
                guess_color_list.pop(i)
            i-=1
                
        #GET HALF ONES
        for code in code_color_list[:]:
            for guess in guess_color_list[:]:
                if code == guess:
                    self.result_list.append("half")
                    code_color_list.remove(code)
                    guess_color_list.remove(guess)
                    break

        while len(self.result_list) < 4:
            self.result_list.append("none")
        self.result_list.sort()
        
        if self.result_list == ["full","full","full","full"]:
            self.won = True
    
    def draw_results(self):
        pos = [self.bbox.right - 120, self.bbox.centery]
        for result in self.result_list:
            if result == "full":
                pygame.draw.circle(self.screen,(0,0,0),pos,10)
            elif result == "half":
                pygame.draw.circle(self.screen,(180,180,180),pos,10)
            elif result == "none":
                pygame.draw.circle(self.screen,(0,0,0),pos,10,width = 2)
            pos[0] += 30
    
    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.bbox,3)
        self.draw_pins()
        self.draw_results()