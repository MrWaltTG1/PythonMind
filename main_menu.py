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
            slider.calculations(int(percentage))

    
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
        
        button_text = ["Back", "Start Game", "Hard", "Normal"]
        self.create_buttons(button_text)
        self.create_sliders()
        self.create_text_box()
    
    def create_buttons(self, button_text):
        self.button_list = []
        
        for button_message in button_text:
            if button_message == "Back": self.button_pos = [(self.button_width /2) + 20 , self.settings.screen_height - 35]
            elif button_message == "Start Game": self.button_pos = [ (self.settings.screen_width -20) - (self.button_width /2) , self.settings.screen_height - 35]
            elif button_message == "Hard" or "Normal" : self.button_pos = [ (self.settings.screen_width -30) - (self.button_width /2) , 280]
            new_button = Button(self.screen, self.settings, button_message, self.button_pos, "sm")
            self.button_list.append(new_button)
            self.button_pos[1] -= self.button_height * 2
    
    def create_sliders(self):
        self.slider_list = []
        
        #Time slider
        min = self.settings.min_time
        default = self.settings.default_time
        max = self.settings.max_time
        mylist = (min,default,max)
        pos = (self.settings.screen_width - 330,100)
        new_slider = Slider(self.settings,self.screen,pos,mylist, is_time=True)
        self.slider_list.append(new_slider)
        
        #max guess slider
        min = 1
        default = 16
        max = 32
        mylist= (min,default,max)
        pos =(self.settings.screen_width - 330, 200)
        new_slider = Slider(self.settings, self.screen,pos,mylist, is_int = True)
        self.slider_list.append(new_slider)
        
    def create_text_box(self):
        pos = (50,50)
        size = (400,500)
        self.text_box = pygame.rect.Rect(pos,size)
        with open('tutorial.txt', 'r') as f:
            msg_list = f.readlines()
        
        self.font = pygame.font.SysFont(self.settings.sm_font_type, 35)
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
                button.button_color = self.settings.sm_button_color_hover
            else:
                button.button_color = self.settings.sm_button_color

        if self.settings.difficulty == 2:
            for button in self.button_list:
                if button.msg == "Normal":
                    button.rect.center = (-100,-100)
                elif button.msg == "Hard":
                    button.rect.center = [ (self.settings.screen_width -30) - (self.button_width /2) , 280]
        elif self.settings.difficulty == 1:
            for button in self.button_list:
                if button.msg == "Hard":
                    button.rect.center = (-100,-100)
                elif button.msg == "Normal":
                    button.rect.center = [ (self.settings.screen_width -30) - (self.button_width /2) , 280]

    def update_sliders(self):
        x,y = pygame.mouse.get_pos()
        for slider in self.slider_list:
            #If mouse is on the slider do:
            if slider.box_rect.collidepoint(x,y):
                pass
                #print("On slider box")
                
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
            if self.settings.difficulty == 2 and button.msg == "Normal":
                continue
            elif self.settings.difficulty == 1 and button.msg == "Hard":
                continue
            else:
                button.draw_button()
        for slider in self.slider_list:
            slider.blitme()
    
    def clicky_wicky_uwu(self, clicked_button):
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
