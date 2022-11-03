import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 900
        self.bg = pygame.image.load("images/black1.bmp")
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        self.rect = self.bg.get_rect()
        
        self.icon = pygame.image.load("images/brain_icon.bmp")
        
        
        #HUD COLOR LIST
        self.hud_colors = {
            'white' : (242,242,242),
            'black' : (25,25,25),
            'light_black' : (50,50,50),
            'grey' : (170,170,170),
            'dark_grey' : (100,100,100),
            'red' : (230,0,0),
            'grey_yellow' : (255, 216, 76)
        }
        
        #Button settings
        self.button_color = self.hud_colors['white']
        self.button_color_hover = self.hud_colors['grey']
        self.text_color = self.hud_colors['black']
        self.font_type, self.font_size = None, 50
        
        
        #Main Menu settings
        self.mm_button_width = 300
        self.mm_button_height = 50
        
        #Option Menu settings
        self.om_button_width = 200
        self.om_button_height = 40

        #Slider settings
        self.sl_box_width = (300, 10)
        self.sl_box_color = self.hud_colors['white']
        self.sl_circle_width = (10,10)
        self.sl_circle_color = self.hud_colors['grey']
        self.sl_text_color = self.hud_colors['white']
        self.sl_font_type, self.sl_font_size = None, 50
        
        #Start Menu settings
        self.sm_button_width = 300
        self.sm_button_height = 50
        self.chalk_font_type, self.chalk_font_size = 'Viner Hand ITC', 25
        
        #Game settings
        """PIN COLORS"""
        self.colors =  {
            "red" : (255,0,0),
            "blue" : (0,0,255),
            "green" : (0,255,0),
            "yellow" : (255,255,0),
            "orange" : (255,165,0),
            "purple" : (153,50,204),
            "brown" : (150,75,0)
            }
        #PIN sizes
        self.small_pin_radius, self.medium_pin_radius, self.big_pin_radius = 20, 40, 60

        self.min_time, self.default_time, self.max_time = 0, 300000, 1800000
        self.min_guesses, self.default_guesses, self.max_guesses = 1,12,50
        self.difficulty = 1 #1 = normal, 2 = hard
        self.shine_image = pygame.image.load("images/shine.bmp")
        self.font_size_timer = 50
        self.code_length = 4
        
        #Game Screen -> Guess Area
        self.guess_box_width = 600
        self.guess_box_height = 120
        self.guess_box_color = self.hud_colors['black']
        #button
        self.gb_button_width = 90
        self.gb_button_height = 30
        self.gb_font_type, self.gb_font_size = None, 20
        
        #Game Screen -> Guess Area -> Guess pins
        self.guess_pin_color_inactive = self.hud_colors['dark_grey']
        self.guess_pin_color_selected = self.hud_colors['grey_yellow']
        self.guess_pin_radius = 35
        self.guess_pin_outline = 6
