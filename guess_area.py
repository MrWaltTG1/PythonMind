import pygame

from button import Button
from elements import Pin


class Guessbox():
    def __init__(self, settings, screen, game_board) -> None:
        self.screen = screen
        self.settings = settings
        self.game_board = game_board
        
        self.color = settings.guess_box_color
        self.width = settings.screen_width * 0.635
        self.height = settings.guess_box_height
        self.size = (self.width, self.height)
        self.guess_pin_list = []
        
        #Create the area and color pins to select from
        self.create_box()
        pos = self.rect.topright
        self.color_pins_area = Guesscolorpinarea(screen,settings, pos)
        self.create_buttons()
        self.create_pins()
    
    def update(self):
        pass
    
    def create_box(self):
        self.rect = pygame.Rect((0,0),self.size)
        self.rect.midbottom = (self.settings.screen_width / 2, self.settings.screen_height)
        self.rect.left = 40
    
    def create_pins(self):
        i=4
        pos = self.rect.midleft  # type: ignore
        while i > 0:
            pos = (pos[0] + self.settings.big_pin_radius + 35, self.rect.midleft[1]) # type: ignore
            new_pin = Pin(self.settings,self.screen,pos,self.settings.guess_pin_color_inactive,self.settings.big_pin_radius)
            self.guess_pin_list.append(new_pin)
            i-=1
    
    def create_buttons(self):       
        #Create a button to push the selection
        pos = self.color_pins_area.bbox.bottomleft
        pos = pos[0] - 30, pos[1] - 30
        self.confirm_box = Button(self.screen,self.settings,"Confirm", pos, "gb")
        self.confirm_box.rect.bottomright = pos
        self.confirm_box.prep_msg("Confirm")
    
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

    def create_fake_guess(self):
            color_list = (self.settings.colors["red"],self.settings.colors["red"],self.settings.colors["red"],self.settings.colors["red"])
            guess_dict = {
                "colors" : color_list,
            }
            self.game_board.guess_list.append(guess_dict)
            self.game_board.new_guess = True
    
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=2)
        pygame.draw.rect(self.screen, self.settings.hud_colors['white'], self.rect, border_radius=2,width = 4)
        self.confirm_box.blitme()

class Guesscolorpinarea():
    def __init__(self,screen,settings, pos):
        self.screen, self.settings = screen, settings
        self.settings = settings
        self.radius = settings.medium_pin_radius

        #Create an invisible box to put the pins in
        bbox_rect = (settings.guess_box_width / 3.5 , settings.guess_box_height - 10)
        self.bbox = pygame.Rect(pos, bbox_rect)
        self.bbox.topright = (pos[0] - 5, pos[1] + 5)

        #Get the coordinates of the pins
        self.pin_pos_list = []
        for x in range(self.bbox.left + self.radius, self.bbox.right, int(self.radius + 10)):
            for y in range(self.bbox.top +int(self.radius/1.5), self.bbox.bottom, int(self.radius + 10)):
                if len(self.pin_pos_list) < 6:
                    self.pin_pos_list.append((x,y))

        #Create the pins
        self.pin_list = []
        i = 1
        pin_colour = None
        for pin_pos in self.pin_pos_list:
            for index, colour in enumerate(self.settings.colors, start=1):
                if index == i:
                    pin_colour = self.settings.colors[colour]
                    break
            i+=1
            new_pin = Pin(settings,screen,pin_pos, pin_colour,self.radius,True)
            self.pin_list.append(new_pin)

    def blitme(self):
        #DEBUG uncomment to see the box the colors are in
        #pygame.draw.rect(self.screen,(250,30,30),self.bbox)
        for pin in self.pin_list:
            pin.blitme()
