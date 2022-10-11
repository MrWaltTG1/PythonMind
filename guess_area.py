
from button import Button
import pygame

class Guessbox():
    def __init__(self, settings, screen, game_board) -> None:
        self.screen = screen
        self.settings = settings
        self.game_board = game_board
        
        self.color = settings.guess_box_color
        self.width = settings.screen_width * 0.9
        self.height = settings.guess_box_height
        self.rect = (self.width, self.height)
        
        self.rect = pygame.Rect((0,0),self.rect)
        self.rect.midbottom = (settings.screen_width / 2, game_board.rect.midbottom[1])
        self.guess_pin_list = []
        i=4
        pos = self.rect.midleft
        while i > 0:
            pos = (pos[0] + (self.settings.guess_pin_radius * 2) + 5, self.rect.midleft[1])
            new_pin = Guesspin(screen,settings,pos)
            self.guess_pin_list.append(new_pin)
            i-=1
        
        #Create the area and color pins to select from
        pos = self.rect.topright
        self.color_pins_area = Guesscolorpinarea(screen,settings, pos)
        
        pos = self.color_pins_area.bbox.bottomleft
        self.confirm_box = Button(screen,settings,"Confirm", pos, "gb")
        self.confirm_box.rect.bottomright = pos
        self.confirm_box.prep_msg("Confirm")
    
    def update(self):
        pass
    
    def confirm_selection(self,button, push = False):
        filled = 0
        self.color_list = []
        for pin in self.guess_pin_list:
            while filled < 4:
                if pin.color is self.settings.guess_pin_color_inactive:
                    filled = -1
                    break
                else:
                    filled += 1
            
            if filled == 4:
                self.color_list.append(pin.color)
                pin.color = self.settings.guess_pin_color_inactive
                push = True
            elif filled == -1:
                print("Please fill all the pins")
                break
        if push:
            self.push_guess()
            
    def push_guess(self):
        guess_dict = {
            "colors" : self.color_list,
        }
        self.game_board.guess_list.append(guess_dict)
        self.game_board.new_guess = True

        
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect, width=5, border_radius=2)
        self.confirm_box.draw_button()

class Guesspin():
    def __init__(self, screen, settings, pos) -> None:
        self.screen = screen
        self.settings = settings
        
        self.color = settings.guess_pin_color_inactive
        self.pos = pos
        self.radius = settings.guess_pin_radius
        self.outline = settings.guess_pin_outline
        
        self.rect = pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, width=self.outline)

class Guesscolorpinarea():
    def __init__(self,screen,settings, pos):
        self.screen = screen
        self.settings = settings
        self.radius = settings.guess_pin_radius / 1.7
        
        #Create an invisible box to put the pins in
        bbox_rect = (settings.guess_box_width / 3.5 , settings.guess_box_height - 10)
        self.bbox = pygame.Rect(pos, bbox_rect)
        self.bbox.topright = (pos[0] - 5, pos[1] + 5)
        
        #Get the coordinates of the pins
        self.pin_pos_list = []
        for x in range(self.bbox.left, self.bbox.right, int(self.radius * 2) + 5):
            x += self.radius + 2
            for y in range(self.bbox.top, self.bbox.bottom, int(self.radius * 2 + 5)):
                y += self.radius + 2
                if len(self.pin_pos_list) < 6:
                    self.pin_pos_list.append((x,y))
        
        self.pin_list = []
        i = 1
        pin_colour = None
        for pin in self.pin_pos_list:
            for index, colour in enumerate(self.settings.colors, start=1):
                if index == i:
                    pin_colour = self.settings.colors[colour]
                    break
            i+=1
            new_pin = Guesspincolor(settings,screen,pin, pin_colour)
            self.pin_list.append(new_pin)
        
        
        
    def blitme(self):
        #DEBUG uncomment to see the box the colors are in
        #pygame.draw.rect(self.screen,(30,30,30),self.bbox)
        for pin in self.pin_list:
            pin.blitme()
        pass
            
        

class Guesspincolor():
    def __init__(self, settings, screen, pos, color) -> None:
        self.screen = screen
        self.settings = settings
        self.radius = settings.guess_pin_radius / 1.7
        self.pos = pos
        self.color = color
        
        self.rect = pygame.draw.circle(self.screen, self.color, self.pos,self.radius)
        
    def blitme(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center,self.radius)