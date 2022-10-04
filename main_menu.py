import pygame
from button import Button

class Main_menu():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.mm_button_width
        self.button_height = settings.mm_button_height
        self.screen = screen
        self.settings = settings
        
        button_amount = 3
        self.create_buttons(button_amount)
    
    def create_buttons(self, button_amount):
        msg = "Start"
        self.new_button = Button(self.screen, self.settings, msg)
    
    def blitme(self):
        #self.screen.blit()
        self.new_button.draw_button()