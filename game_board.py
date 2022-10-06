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
        self.new_guess = None
        self.guess_dict = {}
        i=1
        while i <= 12:
            self.guess_dict[i] = None
            i+=1
        


    
        
    def update(self):
        pos = self.rect.midtop
        for guess in self.guess_dict.values():
            if guess != None:
                self.new_guess = Guess(self.settings,self.screen,pos,colors = guess)
                pos = self.new_guess.bbox.midtop
        
    
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
        for color in self.colors:
            pygame.draw.circle(self.screen,color,(40,40),10)