import random
import pygame

from guess_area import Guesspincolor

class SecretCode():
    def __init__(self,settings,screen) -> None:
        self.settings = settings
        self.screen = screen
        
        pos = (0,0)
        size = (400,100)
        self.bbox_rect = pygame.rect.Rect(pos,size)
        self.bbox_rect.midtop = (self.settings.screen_width / 2, 20)
        self.filled = 0
        
        self.colorlist = list(settings.colors.values())
        
        self.pin_list = []
        pin_pos = self.bbox_rect.midleft
        i=0
        while i < 4:
            random_color = random.choice(self.colorlist)
            if self.settings.difficulty == 1:
                self.colorlist.remove(random_color)
            pin_pos = (pin_pos[0]+ 80, pin_pos[1])
            new_pin = Guesspincolor(self.settings,self.screen,pin_pos,random_color)
            self.pin_list.append(new_pin)
            i+=1
            
    def update(self, won):
        if won:
            self.filled = 2
        self.code_list = []
        for pin in self.pin_list:
            self.code_list.append(pin.color)
        
    def blitme(self):
        for pin in self.pin_list:
            pin.blitme()
        pygame.draw.rect(self.screen,self.settings.hud_colors['white'],self.bbox_rect,width=self.filled)