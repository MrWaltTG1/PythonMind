import pygame

class Slider():
    def __init__(self,settings,screen,pos, msg = "hello") -> None:
        self.screen = screen
        self.settings = settings
        self.pos = pos #Left top position
        #The bounding box settings
        self.box_width = settings.sl_box_width
        self.box_color = settings.sl_box_color
        #The sliding circle settings
        self.circle_width = settings.sl_circle_width
        self.circle_color = settings.sl_circle_color
        
        #Create the rect for the bounding box
        self.box_rect = pygame.Rect(self.pos, self.box_width)
        #Place the sliding circle in the left-middle part of the box
        self.circle_posy = self.box_rect.centery
        self.circle_posx = self.box_rect.left
        self.circle_pos = [self.circle_posx, self.circle_posy]
        
        #Text settings
        self.text_color = settings.sl_text_color
        self.text_font = settings.sl_font_type
        self.font_size = settings.sl_font_size
        self.font = pygame.font.SysFont(self.text_font, self.font_size)
        
        #create text above the slider
        self.msg = msg
        self.prep_msg(self.msg)
        
    def prep_msg(self, msg):
        #check to see if it is an integer or not
        if isinstance(msg, int):
            self.msg = str(msg) + "%"
        else: self.msg = msg
        #transform the text into an image
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #place the message in the middle above the slider
        self.msg_image_rect.midbottom = self.box_rect.midtop
    
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.box_color, self.box_rect)
        pygame.draw.circle(self.screen,self.circle_color,self.circle_pos, radius=5)
        self.screen.blit(self.msg_image, self.msg_image_rect)
