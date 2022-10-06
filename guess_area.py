
from cmath import rect
import math
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
            new_pin = Guesspin(screen,settings,pos)
            self.guess_pin_list.append(new_pin)
            i-=1
        
        #Create the area and color pins to select from
        pos = self.rect.topright
        self.color_pins_area = Guesscolorpinarea(screen,settings, pos)
    
    def update(self):
        pass
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect, width=5, border_radius=2)

class Guesspin():
    def __init__(self, screen, settings, pos) -> None:
        self.screen = screen
        self.settings = settings
        
        self.color = settings.guess_pin_color_inactive
        self.pos = pos
        self.radius = settings.guess_pin_radius
        self.outline = settings.guess_pin_outline
        
        self.rect = pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)

class Guesscolorpinarea():
    def __init__(self,screen,settings, pos):
        self.screen = screen
        self.settings = settings
        self.radius = settings.guess_pin_radius / 1.7
        
        #Create an invisible box to put the pins in
        bbox_rect = (settings.guess_box_width / 3.5 , settings.guess_box_height - 10)
        self.bbox = pygame.Rect(pos, bbox_rect)
        self.bbox.topright = (pos[0] - 5, pos[1] + 5)
        
        #Get the coordinates of the pins
        self.pin_pos_list = []
        for x in range(self.bbox.left, self.bbox.right, int(self.radius * 2) + 5):
            x += self.radius + 2
            for y in range(self.bbox.top, self.bbox.bottom, int(self.radius * 2 + 5)):
                y += self.radius + 2
                if len(self.pin_pos_list) < 6:
                    self.pin_pos_list.append((x,y))
        
        self.pin_list = []
        i = 1
        for pin in self.pin_pos_list:
            for index, colour in enumerate(self.settings.colors, start=1):
                if index == i:
                    pin_colour = self.settings.colors[colour]
                    break
            i+=1
            new_pin = Guesspincolor(settings,screen,pin, pin_colour)
            self.pin_list.append(new_pin)
        
        
        
    def blitme(self):
        #DEBUG uncomment to see the box the colors are in
        #pygame.draw.rect(self.screen,(30,30,30),self.bbox)
        for pin in self.pin_list:
            pin.blitme()
        pass
            
        

class Guesspincolor():
    def __init__(self, settings, screen, pos, color) -> None:
        self.screen = screen
        self.settings = settings
        self.radius = settings.guess_pin_radius / 1.7
        self.pos = pos
        self.color = color
        
        self.rect = pygame.draw.circle(self.screen, self.color, self.pos,self.radius)
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center,self.radius)