import pygame
import game_functions as gf

class Slider():
    def __init__(self,settings,screen,pos,sliderlist, msg = "No message has been given", is_time = False, is_int = False) -> None:
        self.screen = screen
        self.settings = settings
        self.pos = pos #Left top position
        self.percentage = 50
        self.is_time = is_time
        self.is_int = is_int
        self.sliderlist = sliderlist
    
        self.msg = msg
            
        #The bounding box settings
        self.box_width = settings.sl_box_width
        self.box_color = settings.sl_box_color
        #The sliding circle settings
        self.circle_width = settings.sl_circle_width
        self.circle_color = settings.sl_circle_color
        
        #Create the rect for the bounding box
        self.box_rect = pygame.Rect(self.pos, self.box_width)

        #Text settings
        self.text_color = settings.sl_text_color
        self.text_font = settings.sl_font_type
        self.font_size = settings.sl_font_size
        self.font = pygame.font.SysFont(self.text_font, self.font_size)
        
        #create text above the slider
        self.calculations(None)
        
        #Place the sliding circle in the left-middle part of the box
        self.circle_posy = self.box_rect.centery
        self.circle_posx = self.box_rect.left + self.box_rect.width * self.percentage
        self.circle_pos = [self.circle_posx, self.circle_posy]
        
    def prep_msg(self, msg):
        #check to see if it is an integer or not
        if isinstance(msg, int) and not self.is_int:
            self.msg = str(msg) + "%"
        elif isinstance(msg,int) and self.is_int:
            self.msg = str(msg)
        else: self.msg = str(msg)
        #transform the text into an image
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #place the message in the middle above the slider
        self.msg_image_rect.midbottom = self.box_rect.midtop
    
    def calculations(self, new_percent):
        min, default, max = self.sliderlist
        default_percentage = (default - min) / (max - min)
        self.percentage = default_percentage
        
        if new_percent: self.percentage = new_percent
        if self.is_time:
            self.new_ticks = int(max *(self.percentage/100) + min)
            minutes, seconds= gf.convert_ticks_to_time(self.new_ticks)
            msg = str("%s:%s" % (minutes, seconds))
            pass
        elif self.is_int:
            msg = int(max *(self.percentage/100) + min)
        else:
            msg = new_percent
            self.new_ticks = None
        
        self.prep_msg(msg)


    def blitme(self):
        pygame.draw.rect(self.screen, self.box_color, self.box_rect,border_radius= 2)
        pygame.draw.circle(self.screen,self.circle_color,self.circle_pos, radius=5)
        self.screen.blit(self.msg_image, self.msg_image_rect)