import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg = pygame.image.load("images/space.bmp")
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        self.rect = self.bg.get_rect()
        
        
        #Main Menu settings
        self.mm_button_width = 300
        self.mm_button_height = 50
        self.mm_button_color = (139,0,139)
        self.mm_button_color_hover = (75,0,130)
        self.mm_text_color = (230,230,230)
        self.mm_font_type, self.mm_font_size = None, 50
        
        #Option Menu settings
        self.om_button_width = 200
        self.om_button_height = 40
        self.om_button_color = (139,0,139)
        self.om_button_color_hover = (75,0,130)
        self.om_text_color = (230,230,230)
        self.om_font_type, self.om_font_size = None, 50