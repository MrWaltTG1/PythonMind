import pygame
from button import Button
from elements import Pin
from secret_code import SecretCode

class Gameboard():
    def __init__(self, settings,screen) -> None:
        self.screen, self.settings = screen, settings
        
        self.pos = (settings.screen_width / 2, settings.screen_height / 2) #Top left position
        self.width, self.height = settings.screen_width * 0.635, settings.screen_height * 0.85
        self.color = self.settings.hud_colors['white']
        
        self.rect = pygame.Rect(self.pos, (self.width,self.height))
        self.rect.center = self.pos
        self.rect.top += 60
        self.rect.left = 40
        self.new_guess, self.won, self.loss = False,False,False
        self.guess_list,self.empty_guess_list, self.total_guesses, self.secret_code = [],[],[],[]
        self.index = 0
        self.starting_index, self.ending_index = 0,6
        self.fill_empty_guesses()
        self.create_buttons()
        self.create_side_bar()


    def update(self):
        if self.new_guess:
            for guess in self.total_guesses:
                guess.update()
            self.create_guess()
            self.new_guess = False
            
            if len(self.total_guesses) > 6:
                self.starting_index += 1
                self.ending_index += 1
                self.update_side_bar()
            
            
        self.code.update(self.won)

        #UPDATE the new guess positions
        for guess in self.total_guesses:
            if guess.won == True:
                self.won = True
        
        
        
            

    def create_buttons(self):
        self.button_list = []
        msg = '^' 
        size = 30,70
        pos = self.rect.right - 5, self.rect.top + 5
        up_button = Button(self.screen,self.settings,msg,pos,'gb_2')
        up_button.rect.size = size
        up_button.rect.topright = pos
        up_button.msg_image_rect.center = up_button.rect.center
        
        msg = 'v'
        pos = self.rect.right - 5, self.rect.bottom - self.settings.guess_box_height + 8
        down_button = Button(self.screen,self.settings,msg,pos,'gb_2')
        down_button.rect.size = size
        down_button.rect.bottomright = pos
        pygame.transform.rotate(down_button.msg_image, 180)
        down_button.msg_image_rect.center = down_button.rect.center
        
        self.button_list  = [up_button,down_button]
    
    def click(self,button):
        if button.msg == "^":
            if self.ending_index < self.settings.max_guesses and self.starting_index < (len(self.total_guesses) - 6):
                self.starting_index += 1
                self.ending_index += 1
                for guess in self.total_guesses:
                    guess.update(reverse=False)
                self.side_bar_slide_rect.bottom = self.side_bar_slide_rect.top
        elif button.msg == "v":
            if self.starting_index > 0:
                self.starting_index -= 1
                self.ending_index -= 1
                for guess in self.total_guesses:
                    guess.update(reverse=True)
                self.side_bar_slide_rect.top = self.side_bar_slide_rect.bottom
        else:
            print('smth went wrong with the side bar buttons')
        
    
    def create_side_bar(self):
        pos = self.button_list[0].rect.bottomright
        size = 30,self.button_list[1].rect.top - self.button_list[0].rect.bottom
        self.side_bar_rect = pygame.Rect(pos,size)
        self.side_bar_rect.topright = pos
        
    def update_side_bar(self):
        if len(self.total_guesses) > 6:
            self.side_bar_slide_rect = pygame.Rect(self.side_bar_rect.topleft,self.side_bar_rect.size)
            
            x = len(self.total_guesses) - 5
            self.side_bar_slide_rect.height = int(self.side_bar_rect.height / x)


    def fill_empty_guesses(self):
        pos = self.rect.midtop[0], self.rect.midtop[1] + 10
        colors = []
        i=4
        while i > 0:
            colors.append(self.settings.guess_pin_color_inactive)
            i-=1
        i = 6
        while i > 0:
            add_guess = Guess(self.settings,self.screen,pos,colors,0)
            add_guess.create_pins()
            add_guess.create_results()
            self.empty_guess_list.append(add_guess)
            pos = add_guess.bbox.centerx, add_guess.bbox.bottom + 8
            i -= 1

    def create_guess(self):
        if self.guess_list:
            if len(self.guess_list) > 0:
                self.guess_list[self.index]["pos"] = self.rect.midtop[0], self.rect.midtop[1] + 10
                add_guess = Guess(self.settings,self.screen,self.guess_list[self.index]["pos"],self.guess_list[self.index]["colors"],len(self.guess_list))
                #add_guess.bbox.midtop = self.rect.midtop
                add_guess.create_pins()
                add_guess.get_results(self.secret_code)
                add_guess.create_results()
                self.total_guesses.append(add_guess)
                self.index += 1

    def create_secret_code(self):
        self.code = SecretCode(self.settings,self.screen)


    def blitme(self):
        pygame.draw.rect(self.screen,self.settings.hud_colors["black"], self.rect)
        pygame.draw.rect(self.screen,self.color,self.rect, 5)
        pygame.draw.rect(self.screen,self.settings.hud_colors['dark_grey'],self.side_bar_rect)
        if len(self.total_guesses) > 6:
            pygame.draw.rect(self.screen,self.settings.hud_colors['grey'],self.side_bar_slide_rect)
        self.code.blitme()


class Guess():
    def __init__(self, settings,screen, pos, colors, number) -> None:
        self.screen, self.settings, self.colors, self.pos, self.number = screen, settings, colors, pos, number
        self.won = False
        self.width, self.height = (settings.screen_width * 0.635) - 10, 100
        
        self.bbox = pygame.Rect(pos,(self.width,self.height))
        self.bbox.midtop = pos
        self.color = self.settings.hud_colors['black']
        self.original_surf = self.settings.shine_image
        self.create_indent_box()
    
    def update(self, reverse = False):
        if not reverse:
            self.bbox.top += self.bbox.height + 8
            self.indent_rect.top += self.bbox.height + 8
        else:
            self.bbox.top -= self.bbox.height + 8
            self.indent_rect.top -= self.bbox.height + 8
        self.create_indent_box()
        self.create_pins()
        self.create_results()
    
    def create_indent_box(self):
        pos = self.bbox.center
        size = self.width * 0.9, self.height * 0.9
        self.indent_rect = pygame.Rect(pos,size)
        self.indent_rect.center = pos
        
        
        self.coord1 = (self.indent_rect.right - self.indent_rect.width / 4.5), self.indent_rect.top +1
        self.coord2 = (self.indent_rect.right - (self.indent_rect.width / 4.5 *2)), self.indent_rect.top +1
        self.coord3 = (self.indent_rect.right - (self.indent_rect.width / 4.5 *1.5)), self.indent_rect.top + self.height * 0.3
        self.indent_indent_coords_top = self.coord1, self.coord2, self.coord3
        self.indent_indent_coords_top2 = (self.coord1[0], self.coord1[1] - 1), (self.coord2[0], self.coord2[1] - 1), (self.coord3[0],self.coord3[1] - 5)
        
        self.coord4 = (self.indent_rect.right - self.indent_rect.width / 4.5), self.indent_rect.bottom -3
        self.coord5 = (self.indent_rect.right - (self.indent_rect.width / 4.5 *2)), self.indent_rect.bottom -3
        self.coord6 = (self.indent_rect.right - (self.indent_rect.width / 4.5 *1.5)), self.indent_rect.bottom - self.height * 0.3
        self.indent_indent_coords_bottom = self.coord4, self.coord5, self.coord6
        self.indent_indent_coords_bottom2 = (self.coord4[0], self.coord4[1] +3), (self.coord5[0], self.coord5[1] +3), (self.coord6[0],self.coord6[1] + 5)

        self.font = pygame.font.SysFont(self.settings.font_type, self.settings.font_size)
        self.msg_image = self.font.render(str(self.number),True,self.settings.hud_colors["red"])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.indent_rect.left - 20, self.bbox.centery
        
    def create_pins(self):
        self.pin_list = []
        pos = (self.bbox.midleft[0]  + self.settings.big_pin_radius + 30, self.bbox.midleft[1])
        for color in self.colors:
            new_pin = Pin(self.settings,self.screen,pos,color,self.settings.big_pin_radius)
            self.pin_list.append(new_pin)
            pos = (pos[0] + self.settings.big_pin_radius + 35, self.bbox.midleft[1])
    
    
    def get_results(self, secret_code):
        for code in secret_code:
            print(code.color)
        
        self.result_list, code_color_list, guess_color_list = [], [], []
        for code in secret_code:
            code_color_list.append(code.color)
        for color in self.colors:
            guess_color_list.append(color)
        
        i = 3
        #GET FULL ONES
        while i > -1:
            if code_color_list[i] == guess_color_list[i]:
                self.result_list.append("full")
                code_color_list.pop(i)
                guess_color_list.pop(i)
            i-=1
                
        #GET HALF ONES
        for code in code_color_list[:]:
            for guess in guess_color_list[:]:
                if code == guess:
                    self.result_list.append("half")
                    code_color_list.remove(code)
                    guess_color_list.remove(guess)
                    break
        
        #Fill the rest with empty spaces
        while len(self.result_list) < 4:
            self.result_list.append("none")
        if self.settings.difficulty == 1:
            self.result_list.sort()

        #Checks to see if the game has been won by guessing the correct code
        if self.result_list == ["full","full","full","full"]:
            self.won = True

    def create_results(self):
        pos = [self.bbox.right - 155, self.bbox.centery]
        size = [155, self.bbox.height]
        self.result_rect = pygame.rect.Rect(pos, size)  # type: ignore
        self.result_rect.midleft = pos  # type: ignore


        pos = [self.bbox.right - 190, self.bbox.centery - 7.5]
        self.result_pin_list = []
        try:
            for result in self.result_list:
                if result == "full":
                    new_result_pin = Pin(self.settings,self.screen,pos,self.settings.hud_colors['red'],self.settings.small_pin_radius)
                    self.result_pin_list.append(new_result_pin)

                elif result == "half":
                    new_result_pin = Pin(self.settings,self.screen,pos,self.settings.hud_colors['white'],self.settings.small_pin_radius)
                    self.result_pin_list.append(new_result_pin)

                elif result == "none":
                    new_result_pin = Pin(self.settings,self.screen,pos,self.settings.guess_pin_color_inactive,self.settings.small_pin_radius)
                    self.result_pin_list.append(new_result_pin)

                pos[0] += 28
        except:
            i=4
            while i > 0:
                new_result_pin = Pin(self.settings,self.screen,pos,self.settings.guess_pin_color_inactive,self.settings.small_pin_radius)
                self.result_pin_list.append(new_result_pin)
                pos[0] += 28
                i-=1
        self.result_pin_list[1].rect.centery, self.result_pin_list[3].rect.centery = pos[1] +15, pos[1]+15
        self.result_pin_list[1].rect_big.centery, self.result_pin_list[3].rect_big.centery = pos[1] +15, pos[1]+15

    def draw_indent_box(self):
        pygame.draw.rect(self.screen,self.settings.hud_colors["light_black"],self.indent_rect, border_radius=10)
        pygame.draw.rect(self.screen,self.settings.hud_colors["dark_grey"],self.indent_rect,width=4, border_radius=10)
        
        #Top indent indent
        pygame.draw.polygon(self.screen,self.settings.hud_colors["black"],self.indent_indent_coords_top)
        pygame.draw.polygon(self.screen,self.settings.hud_colors["dark_grey"],self.indent_indent_coords_top,width=4)
        pygame.draw.polygon(self.screen,self.settings.hud_colors["black"],self.indent_indent_coords_top2)
        #Bottom indent indent
        pygame.draw.polygon(self.screen,self.settings.hud_colors["black"],self.indent_indent_coords_bottom)
        pygame.draw.polygon(self.screen,self.settings.hud_colors["dark_grey"],self.indent_indent_coords_bottom,width=4)
        pygame.draw.polygon(self.screen,self.settings.hud_colors["black"],self.indent_indent_coords_bottom2)

        if self.number != 0:
            self.screen.blit(self.msg_image,self.msg_image_rect)
        
    def blitme(self):
        self.draw_indent_box()
        for pin in self.pin_list:
            pin.blitme()
        #pygame.draw.rect(self.screen,self.settings.hud_colors['dark_grey'],self.result_rect)
        for result in self.result_pin_list:
            result.blitme()