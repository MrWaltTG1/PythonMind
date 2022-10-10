import pygame

class Gameboard():
    def __init__(self, settings,screen) -> None:
        self.screen = screen
        self.settings = settings
        
        self.pos = (settings.screen_width / 2, settings.screen_height / 2) #Top left position
        self.width = settings.screen_width * 0.9
        self.height = settings.screen_height * 0.9
        self.color = (92, 64, 51)
        
        self.rect = pygame.Rect(self.pos, (self.width,self.height))
        self.rect.center = self.pos
        self.new_guess = False
        self.guess_list = []
        self.total_guesses = []
        self.index = 0
        
        
    def update(self):
        if self.new_guess:
            for guess in self.total_guesses:
                guess.bbox.midtop = guess.bbox.midbottom
            self.create_guess()
            self.new_guess = False


        #UPDATE the new guess positions
        
    def create_guess(self):
        if self.guess_list:
            if len(self.guess_list) > 0:
                self.guess_list[self.index]["pos"] = (0,0)
                add_guess = Guess(self.settings,self.screen,self.guess_list[self.index]["pos"],self.guess_list[self.index]["colors"])
                add_guess.bbox.midtop = self.rect.midtop
                self.total_guesses.append(add_guess)
                self.index += 1
            
    
    def blitme(self): 
        pygame.draw.rect(self.screen,self.color,self.rect, 5)
        #self.new_guess.blitme()
        
class Guess():
    def __init__(self, settings,screen, pos, colors) -> None:
        self.screen = screen
        self.settings = settings
        
        self.colors = colors
        self.pos = pos
        self.width, self.height = (settings.screen_width * 0.9) - 10, 100
        
        self.bbox = pygame.Rect(pos,(self.width,self.height))
        self.bbox.midtop = pos
        self.color = (51,120,59)
        
    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.bbox,3)
        pos = (self.bbox.midleft[0]  + self.settings.guess_pin_radius * 2 + 20, self.bbox.midleft[1])
        for color in self.colors:
            pygame.draw.circle(self.screen,color,pos,self.settings.guess_pin_radius)
            pos = (pos[0] + self.settings.guess_pin_radius * 2 + 20, self.bbox.midleft[1])