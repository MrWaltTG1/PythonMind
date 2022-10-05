import sys
import pygame
from button import Button

class Main_menu():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.mm_button_width
        self.button_height = settings.mm_button_height
        self.screen = screen
        self.settings = settings
        
        self.active = True
        
        button_text = ["Start", "Options", "Quit"]
        self.create_buttons(button_text)
    
    def create_buttons(self, button_text):
        self.button_list = []
        self.button_pos = [self.settings.screen_width / 2, 300]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "mm")
            self.button_list.append(new_button)
            self.button_pos[1] += self.button_height * 2
    
    def update(self, menu_list):
        self.option_menu = menu_list[1]
        
        self.update_buttons()
        
    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        mouse_pos = (x,y)
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.mm_button_color_hover
            else:
                button.button_color = self.settings.mm_button_color
    
    def blitme(self):
        for button in self.button_list:
            button.draw_button()
            
    def clicky_wicky_uwu(self, clicked_button):
        if clicked_button.msg == "Start":
            self.active = False
        elif clicked_button.msg == "Options":
            self.active = False
            self.option_menu.active = True
        elif clicked_button.msg == "Quit":
            sys.exit()

class Options():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.om_button_width
        self.button_height = settings.om_button_height
        self.screen = screen
        self.settings = settings
        
        self.active = False
        
        button_text = ["Back"]
        self.create_buttons(button_text)
    
    def create_buttons(self, button_text):
        self.button_list = []
        self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "om")
            self.button_list.append(new_button)
            self.button_pos[1] += self.button_height * 2
    
    def update(self, menu_list):
        self.main_menu = menu_list[0]
        self.update_buttons()
        
    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        mouse_pos = (x,y)
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.mm_button_color_hover
            else:
                button.button_color = self.settings.mm_button_color
    
    def blitme(self):
        for button in self.button_list:
            button.draw_button()
            
    def clicky_wicky_uwu(self, clicked_button):
        if clicked_button.msg == "Back":
            self.active = False
            self.main_menu.active = True
            
class Start_menu():
    pass