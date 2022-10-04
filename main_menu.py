import pygame
from button import Button

class Main_menu():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.mm_button_width
        self.button_height = settings.mm_button_height
        self.screen = screen
        self.settings = settings
        

        
        button_text = ["Start", "Options", "Quit"]
        self.create_buttons(button_text)
    
    def create_buttons(self, button_text):
        self.button_list = []
        self.button_pos = [self.settings.screen_width / 2, 300]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos)
            self.button_list.append(new_button)
            self.button_pos[1] += self.button_height * 2
        #self.new_button.rect = self.new_button.get_rect()
    
    def blitme(self):
        for button in self.button_list:
            button.draw_button()
            
    def clicky_wicky_uwu(self):
        print("YAY")