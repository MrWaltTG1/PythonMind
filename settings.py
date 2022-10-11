import pygame

class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg = pygame.image.load("images/whitebig.bmp")
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
        #Slider settings
        self.sl_box_width = (300, 10)
        self.sl_box_color = (75,0,130)
        self.sl_circle_width = (10,10)
        self.sl_circle_color = (139,0,139)
        self.sl_text_color = (0,0,0)
        self.sl_font_type, self.sl_font_size = None, 50
        
        #Start Menu settings
        self.sm_button_width = 300
        self.sm_button_height = 50
        self.sm_button_color = (139,0,139)
        self.sm_button_color_hover = (75,0,130)
        self.sm_text_color = (230,230,230)
        self.sm_font_type, self.sm_font_size = None, 50
        
        #Game settings
        self.colors =  {
            "red" : (255,0,0),
            "blue" : (0,0,255),
            "green" : (0,255,0),
            "yellow" : (255,255,0),
            "orange" : (255,165,0),
            "purple" : (153,50,204)
            }
        self.min_time = 0
        self.default_time = 300000 #5 mins   #In ms
        self.max_time = 1800000 #30 mins
        
        #Game Screen -> Guess Area
        self.guess_box_width = 600
        self.guess_box_height = 100
        self.guess_box_color =(50,50,50)
        #button
        self.gb_button_width = 80
        self.gb_button_height = 20
        self.gb_button_color = (139,0,139)
        self.gb_button_color_hover = (75,0,130)
        self.gb_text_color = (230,230,230)
        self.gb_font_type, self.gb_font_size = None, 20
        
        #Game Screen -> Guess Area -> Guess pins
        self.guess_pin_color_inactive = (100,100,100)
        self.guess_pin_radius = 35
        self.guess_pin_outline = 0
