
import pygame

class Guessbox():
    def __init__(self, settings, screen, menu_dict) -> None:
        self.screen = screen
        self.settings = settings
        self.menu_dict = menu_dict
        
        self.color = (50,50,50)
        self.width = 500
        self.height = 100
        self.rect = (self.width, self.height)
        self.pos = (0,0)
        
        self.rect = pygame.Rect(self.pos,self.rect)
        self.rect.midbottom = (settings.screen_width / 2, settings.screen_height)
        self.new_pin = Guesspin(screen,settings,self)
    
    def update(self):
        self.new_pin.blitme()
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect, width=5, border_radius=2)

class Guesspin():
    def __init__(self, screen, settings, bbox) -> None:
        self.screen = screen
        self.settings = settings
        
        self.color = settings.guess_pin_color_inactive
        self.pos = bbox.rect.midleft
        self.radius = settings.guess_pin_radius
        self.outline = settings.guess_pin_outline
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)