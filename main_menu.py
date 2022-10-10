import sys
import pygame
from button import Button
from slider import Slider

class Main_menu():
    #The main men
    def __init__(self, settings, screen) -> None:
        self.screen = screen
        self.settings = settings
        
        self.active = True
        
        self.button_height = settings.mm_button_height
        #these are the options to select from
        button_text = ["Start", "Options", "Quit"]
        self.create_buttons(button_text)
    
    def create_buttons(self, button_text):
        #Create a button for every option given
        self.button_list = []
        self.button_pos = [self.settings.screen_width / 2, 300]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "mm")
            self.button_list.append(new_button)
            self.button_pos[1] += self.button_height * 2
    
    def update(self, menu_dict):
        self.option_menu = menu_dict["option_menu"]
        self.start_menu = menu_dict["start_menu"]
        
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
            self.start_menu.active = True
        elif clicked_button.msg == "Options":
            self.active = False
            self.option_menu.active = True
        elif clicked_button.msg == "Quit":
            sys.exit()

"""
OPTION MENU STUFF
"""

class Options():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.om_button_width
        self.button_height = settings.om_button_height
        self.screen = screen
        self.settings = settings
        
        self.active = False
        
        button_text = ["Back"]
        self.create_buttons(button_text)
        self.create_slider()
        
    
    def create_buttons(self, button_text):
        self.button_list = []
        self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "om")
            self.button_list.append(new_button)
            self.button_pos[1] -= self.button_height * 2
    
    def create_slider(self):
        pos = (100,500)
        self.slider_list = []
        new_slider = Slider(self.settings,self.screen,pos)
        self.slider_list.append(new_slider)
    
    def update(self, menu_dict):
        self.main_menu = menu_dict["main_menu"]
        self.update_buttons()
        self.update_sliders()
        
    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.om_button_color_hover
            else:
                button.button_color = self.settings.om_button_color
    
    def update_sliders(self):
        x,y = pygame.mouse.get_pos()
        for slider in self.slider_list:
            #If mouse is on the slider do:
            if slider.box_rect.collidepoint(x,y):
                pass
                #print("On slider box")
                
            percent_max = slider.box_rect.width
            percentage = 100 * (slider.circle_pos[0] - slider.box_rect.left) / percent_max
            slider.prep_msg(int(percentage))


    
    def blitme(self):
        for button in self.button_list:
            button.draw_button()
        
        for slider in self.slider_list:
            slider.blitme()
            
    def clicky_wicky_uwu(self, clicked_button):
        if clicked_button.msg == "Back":
            self.active = False
            self.main_menu.active = True
        elif clicked_button.msg == "Resolution":
            pass
            self.resolution_dd()

    def resolution_dd(self):
        """THIS DOES NOT WORK"""
        self.resolution_list = ((1920,1080),(800,600))
        
        current_resolution = (self.settings.screen_width, self.settings.screen_height)
        new_resolution = self.resolution_list[0]
        
        self.settings.rect = new_resolution
        self.settings.bg = pygame.transform.scale(self.settings.bg, new_resolution)
            
"""

START MENU STUFF


"""

class Start_menu():
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.sm_button_width
        self.button_height = settings.sm_button_height
        self.screen = screen
        self.settings = settings
        
        self.active = False
        
        button_text = ["Back", "Start Game"]
        self.create_buttons(button_text)
    
    def create_buttons(self, button_text):
        self.button_list = []
        
        for button_message in button_text:
            if button_message == "Back": self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
            if button_message == "Start Game": self.button_pos = [ (self.settings.screen_width -20) - (self.button_width /2) , self.settings.screen_height - 35]
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "sm")
            self.button_list.append(new_button)
            self.button_pos[1] -= self.button_height * 2
    
    def update(self, menu_dict, game_screen):
        self.main_menu = menu_dict["main_menu"]
        self.game_screen = game_screen
        self.update_buttons()
        
    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.sm_button_color_hover
            else:
                button.button_color = self.settings.sm_button_color
    
    def blitme(self):
        for button in self.button_list:
            button.draw_button()
            
    def clicky_wicky_uwu(self, clicked_button):
        if clicked_button.msg == "Back":
            self.active = False
            self.main_menu.active = True
        elif clicked_button.msg == "Start Game":
            self.active = False
            self.game_screen.active = True
            self.game_screen.create_timer()
            