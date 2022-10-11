import pygame

class Button():
    
    def __init__(self, screen, settings, msg, pos, id):
        self.screen= screen
        self.screen_rect = screen.get_rect()
        
        self.pos = pos
        self.msg = msg
        
        if id == "mm" or id == "gs":
            self.width, self.height = settings.mm_button_width, settings.mm_button_height
            self.button_color = settings.mm_button_color
            self.text_color = settings.mm_text_color
            self.font_type = settings.mm_font_type
            self.font_size = settings.mm_font_size
        elif id == "om":
            self.width, self.height = settings.om_button_width, settings.om_button_height
            self.button_color = settings.om_button_color
            self.text_color = settings.om_text_color
            self.font_type = settings.om_font_type
            self.font_size = settings.om_font_size
        elif id == "sm":
            self.width, self.height = settings.sm_button_width, settings.sm_button_height
            self.button_color = settings.sm_button_color
            self.text_color = settings.sm_text_color
            self.font_type = settings.sm_font_type
            self.font_size = settings.sm_font_size
        elif id == "gb":
            self.width, self.height = settings.gb_button_width, settings.gb_button_height
            self.button_color = settings.gb_button_color
            self.text_color = settings.gb_text_color
            self.font_type = settings.gb_font_type
            self.font_size = settings.gb_font_size
        
        
        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = pos
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)