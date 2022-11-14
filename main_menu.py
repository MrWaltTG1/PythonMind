import sys

import pygame

import game_functions as gf
from button import Button
from slider import Slider


class Main_menu():
    """The class containing the main menu"""
    def __init__(self, settings, screen) -> None:
        self.screen, self.settings = screen,settings
        self.active = True
        
        self.button_height = settings.mm_button_height
        #these are the options to select from
        button_text = ["Start", "Quit"]
        self.create_buttons(button_text)
        self.create_text()
    
    def create_buttons(self, button_text):
        """Create a button for every string given"""
        self.button_list = []
        self.button_pos = [self.settings.screen_width / 2, 300]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "mm")
            self.button_list.append(new_button)
            self.button_pos[1] += self.button_height * 2
    
    def create_text(self):
        """Adds various textboxes"""
        self.textbox_list_list = []
        pos = self.settings.rect.centerx, self.settings.rect.centery - 300
        text = "PythonMind"
        size = 500,200
        self.textbox_list1 = gf.create_text_box(self.settings,pos,size,text,font_size = 100,text_color=self.settings.hud_colors["white"])
        self.textbox_list_list.append(self.textbox_list1)
        
        pos = self.settings.rect.centerx, self.settings.rect.centery - 230
        text = "The challenging game of logic and deduction"
        self.textbox_list2 = gf.create_text_box(self.settings,pos,size,text,font_size = 50,text_color=self.settings.hud_colors["white"])
        self.textbox_list_list.append(self.textbox_list2)
        
        pos = self.settings.rect.centerx, self.settings.rect.centery + 230
        text = "Can you crack the code?"
        self.textbox_list3 = gf.create_text_box(self.settings,pos,size,text,font_size = 50,text_color=self.settings.hud_colors["white"])
        self.textbox_list_list.append(self.textbox_list3)
        
    def update(self, menu_dict):
        self.option_menu = menu_dict["option_menu"]
        self.start_menu  = menu_dict["start_menu"]
        
        self.update_buttons()
        
    def update_buttons(self):
        """Updates the colors of the buttons"""
        x,y  = pygame.mouse.get_pos()
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.button_color_hover
            else:
                button.button_color = self.settings.button_color
    
    def blitme(self):
        """draws the necessary things"""
        for button in self.button_list:
            button.blitme()
        for list in self.textbox_list_list:
            self.screen.blit(list[1][0],list[1][1])


    def click(self, clicked_button):
        """Does x when clicked on y button"""
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
    """The class containing the options menu"""
    def __init__(self, settings, screen) -> None:
        self.button_width = settings.om_button_width
        self.button_height = settings.om_button_height
        self.screen, self.settings = screen, settings
        self.active = False
        
        button_text = ["Back"]
        self.create_buttons(button_text)
        self.create_slider()
        

    def create_buttons(self, button_text: list) -> None:
        self.button_list = []
        self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
        for button_message in button_text:
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "om")
            self.button_list.append(new_button)
            self.button_pos[1] -= self.button_height * 2
    
    def create_slider(self):
        pos = (100,500)
        self.slider_list = []
        #min, default, max
        sliderlist = (0,50,100)
        new_slider = Slider(self.settings,self.screen,pos,sliderlist)
        self.slider_list.append(new_slider)
    
    def update(self, menu_dict):
        self.main_menu = menu_dict["main_menu"]
        self.update_buttons()
        self.update_sliders()
        
    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.button_color_hover
            else:
                button.button_color = self.settings.button_color
    
    def update_sliders(self):
        """Update the value in the sliders"""
        for slider in self.slider_list:
            percent_max = slider.box_rect.width
            percentage = 100 * (slider.circle_pos[0] - slider.box_rect.left) / percent_max
            slider.calculations(int(percentage))
    
    def blitme(self):
        for button in self.button_list:
            button.blitme()
        
        for slider in self.slider_list:
            slider.blitme()
            
    def click(self, clicked_button):
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
    """The class containing the starting menu"""
    def __init__(self, settings, screen) -> None:
        self.button_width, self.button_height = settings.sm_button_width, settings.sm_button_height
        self.screen, self.settings = screen, settings
        self.active = False
        
        button_text = ["Back", "Start Game", "Hard", "Normal"]
        self.create_buttons(button_text)
        self.create_sliders()
        self.create_text_box()
    
    def create_buttons(self, button_text):
        self.button_list = []
        self.diff_button_center = 340
        for button_message in button_text:
            if button_message == "Back": self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
            elif button_message == "Start Game": self.button_pos = [ (self.settings.screen_width -20) - (self.button_width /2) , self.settings.screen_height - 35]
            elif button_message == "Hard" or button_message == "Normal" :
                self.button_pos = [ (self.settings.screen_width -30) - (self.button_width /2) , self.diff_button_center]
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "sm")
            if new_button.msg == "Hard" or new_button.msg == "Normal" :
                text = "Difficulty"
                new_button.create_text_box(text)
            else:
                text = ""
            self.button_list.append(new_button)
            self.button_pos[1] -= self.button_height * 2
    
    def create_sliders(self):
        self.slider_list = []
        
        #Time slider
        min, default, max = self.settings.min_time, self.settings.default_time, self.settings.max_time
        mylist = (min,default,max)
        pos = (self.settings.screen_width - 330,100)
        new_slider = Slider(self.settings,self.screen,pos,mylist, is_time=True)
        new_slider.create_text_box("Set the time")
        self.slider_list.append(new_slider)

        #max guess slider
        min, default, max = self.settings.min_guesses, self.settings.default_guesses, self.settings.max_guesses
        mylist= (min,default,max)
        pos =(self.settings.screen_width - 330, 200)
        new_slider = Slider(self.settings, self.screen,pos,mylist, is_int = True)
        new_slider.create_text_box("Set the maximum guesses")
        self.slider_list.append(new_slider)

    def create_text_box(self):
        pos = (50,50)
        size = (700,900)
        self.text_box = pygame.rect.Rect(pos,size)
        with open('tutorial.txt', 'r') as f:
            msg_list = f.readlines()

        self.font = pygame.font.SysFont(self.settings.chalk_font_type, self.settings.chalk_font_size)
        self.text_rect_list = []
        for msg in msg_list:
            msg = msg.splitlines()
            self.msg_image = self.font.render(msg[0], True, self.settings.hud_colors['white'])
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.width = self.text_box.width
            self.msg_image_rect.midtop = self.text_box.midtop
            if self.text_rect_list:
                self.msg_image_rect.midtop = self.text_rect_list[-1][1].midbottom
            self.text_rect_list.append([self.msg_image,self.msg_image_rect])


    def update(self, menu_dict, game_screen):
        self.main_menu = menu_dict["main_menu"]
        self.game_screen = game_screen
        self.update_buttons()
        self.update_sliders()

    def update_buttons(self):
        x,y  = pygame.mouse.get_pos()
        for button in self.button_list:
            if button.rect.collidepoint(x,y):
                button.button_color = self.settings.button_color_hover
            else:
                button.button_color = self.settings.button_color

        #Move the button off/on-screen when needed
        if self.settings.difficulty == 2:
            for button in self.button_list:
                if button.msg == "Normal":
                    button.rect.center = (-100,-100)
                elif button.msg == "Hard":
                    button.rect.center = [ (self.settings.screen_width -30) - (self.button_width /2) , self.diff_button_center]
        elif self.settings.difficulty == 1:
            for button in self.button_list:
                if button.msg == "Hard":
                    button.rect.center = (-100,-100)
                elif button.msg == "Normal":
                    button.rect.center = [ (self.settings.screen_width -30) - (self.button_width /2) , self.diff_button_center]

    def update_sliders(self):
        for slider in self.slider_list:
            percent_max = slider.box_rect.width
            percentage = 100 * (slider.circle_pos[0] - slider.box_rect.left) / percent_max
            
            slider.percentage = percentage
            slider.calculations(int(percentage))
            if slider.is_int == True:
                self.settings.max_guesses = int(slider.msg)


    def blitme(self):
        #pygame.draw.rect(self.screen,(0,0,0),self.text_box,width=2)
        for msg in self.text_rect_list:
            self.screen.blit(msg[0],msg[1])
        for button in self.button_list:
            #Dont draw the normal/hard buttons when not needed
            if self.settings.difficulty == 2 and button.msg == "Normal":
                continue
            elif self.settings.difficulty == 1 and button.msg == "Hard":
                continue
            else:
                button.blitme()
        for slider in self.slider_list:
            slider.blitme()

    def click(self, clicked_button):
        if clicked_button.msg == "Back":
            self.active = False
            self.main_menu.active = True
        elif clicked_button.msg == "Start Game":
            self.active = False
            self.game_screen.active = True
            self.game_screen.create_timer(self.slider_list[0].new_ticks)
            self.game_screen.game_board.create_secret_code()
            self.game_screen.game_board.secret_code = self.game_screen.game_board.code.pin_list

        elif clicked_button.msg == "Normal":
            self.settings.difficulty = 2
        elif clicked_button.msg == "Hard":
            self.settings.difficulty = 1
