
import pygame

class Guessbox():
    def __init__(self, settings, screen, menu_dict) -> None:
        self.screen = screen
        self.settings = settings
        self.menu_dict = menu_dict
        
        self.color = settings.guess_box_color
        self.width = settings.guess_box_width
        self.height = settings.guess_box_height
        self.rect = (self.width, self.height)
        
        self.rect = pygame.Rect((0,0),self.rect)
        self.rect.midbottom = (settings.screen_width / 2, settings.screen_height)
        self.guess_pin_list = []
        i=4
        pos = self.rect.midleft
        while i > 0:
            pos = (pos[0] + (self.settings.guess_pin_radius * 2) + 5, self.rect.midleft[1])
            new_pin = Guesspin(screen,settings,self,pos)
            self.guess_pin_list.append(new_pin)
            i-=1
        
        pin_dict = {
            "red",
            "blue",
            "green",
            "yellow",
            "orange",
            "purple"
            }
        for color in pin_colors:
            new_color_pin = Guesscolorpin(screen,settings,color)

    
    def update(self):
        for pin in self.guess_pin_list:
            pin.blitme()
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect, width=5, border_radius=2)

class Guesspin():
    def __init__(self, screen, settings, bbox, pos) -> None:
        self.screen = screen
        self.settings = settings
        
        self.color = settings.guess_pin_color_inactive
        self.pos = pos
        self.radius = settings.guess_pin_radius
        self.outline = settings.guess_pin_outline
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)

class Guesscolorpin():
    def __init__(self,screen,settings,color):
        self.screen = screen
        self.settings = settings
        
        