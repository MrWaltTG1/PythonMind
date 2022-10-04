import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg = pygame.image.load("images/space.bmp")
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        self.rect = self.bg.get_rect()
        
        
        #Main Menu settings
        self.mm_button_width = 150
        self.mm_button_height = 50