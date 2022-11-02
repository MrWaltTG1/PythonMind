import sys
import pygame

from elements import Pin


def update_screen(settings, screen, menu_dict, game_screen):

    screen.blit(settings.bg, settings.rect)

    if menu_dict["main_menu"].active:
        menu_dict["main_menu"].blitme()
    elif menu_dict["option_menu"].active:
        menu_dict["option_menu"].blitme()
    elif menu_dict["start_menu"].active:
        menu_dict["start_menu"].blitme()
    else:
        game_screen.game_board.blitme()
        game_screen.back_button.blitme()
        game_screen.draw_timer()
        for guess in game_screen.game_board.empty_guess_list:
            guess.blitme()
        for guess in game_screen.game_board.total_guesses[game_screen.game_board.starting_index: game_screen.game_board.ending_index]:
            guess.blitme()
        for button in game_screen.game_board.button_list:
            button.blitme()
        game_screen.guess_box.blitme()
        for pin in game_screen.guess_box.guess_pin_list:
            pin.blitme()
        game_screen.guess_box.color_pins_area.blitme()

        #Draw win condition
        try:
            game_screen.winscreen.blitme()
        except:
            #Draw lose condition
            try:
                game_screen.losescreen.blitme()
            except:
                pass
            

    #display the last drawn screen
    pygame.display.flip()

def check_events(settings, screen, menu_dict, game_screen):
    for event in pygame.event.get():
        #If event is quit then quit
        if event.type == pygame.QUIT:
            sys.exit()
        #Here go all the other event checks
        #FOR CLICKING THE MOUSE (ONE TIME EVENT)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_down_events(event, settings,screen, menu_dict, game_screen)
        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouse_up_events(event, settings,screen, menu_dict, game_screen)
    
    #FOR HOLDING DOWN THE MOUSE
    if pygame.mouse.get_pressed()[0]:
        check_mouse_hold_events(settings,screen,menu_dict, game_screen, hold=True)



def check_mouse_down_events(event, settings,screen, menu_dict, game_screen):
    #Function for mouse clicks
    #Get the x and y location of where has been clicked
    x, y = event.pos

    if event.button == 1: #LEFT CLICK
        #MENU INTERACTIONS
        if menu_dict["main_menu"].active:
            for button in menu_dict["main_menu"].button_list:
                if button.rect.collidepoint(x,y):
                    menu_dict["main_menu"].click(button)
                    break
        elif menu_dict["option_menu"].active:
            for button in menu_dict["option_menu"].button_list:
                if button.rect.collidepoint(x,y):
                    menu_dict["option_menu"].click(button)
                    break
            for slider in menu_dict["option_menu"].slider_list:
                if slider.box_rect.collidepoint(x,y):
                    slider.circle_pos[0] = x
        elif menu_dict["start_menu"].active:
            for button in menu_dict["start_menu"].button_list:
                if button.rect.collidepoint(x,y):
                    menu_dict["start_menu"].click(button)
                    break
            for slider in menu_dict["start_menu"].slider_list:
                if slider.box_rect.collidepoint(x,y):
                    slider.circle_pos[0] = x

        #END OF MENU INTERACTIONS
        # ----------------------
        #GAME SCREEN INTERACTIONS

        elif game_screen.active:
            #Create a new colored pin when left MOUSEBUTTONDOWN, and subsequently remove it when left MOUSEBUTTONUP
            if game_screen.guess_box.rect.collidepoint(x,y):
                for pin in game_screen.guess_box.color_pins_area.pin_list:
                    if pin.rect.collidepoint(x,y):
                        new_pin = create_draggable_pin(settings,screen,pos=(x,y),color = pin.color)
                        game_screen.guess_box.color_pins_area.pin_list.append(new_pin)
                        break
                if game_screen.guess_box.confirm_box.rect.collidepoint(x,y):
                    game_screen.guess_box.confirm_selection(game_screen.guess_box.confirm_box)
            elif game_screen.game_board.rect.collidepoint(x,y):
                for button in game_screen.game_board.button_list:
                    if button.rect.collidepoint(x,y):
                        game_screen.game_board.click(button)


            game_screen.click((x,y))


def check_mouse_up_events(event, settings,screen, menu_dict, game_screen):
    x,y = event.pos
    if event.button == 1: #LEFT CLICK
        #Disables the hold feature of holding down the mouse button
        check_mouse_hold_events(settings,screen,menu_dict, game_screen, hold=False)

def check_mouse_hold_events(settings,screen,menu_dict,game_screen, hold):
    #Function for holding down the mouse button
    x,y = pygame.mouse.get_pos()
    if hold:
        #if event.button == 1: #LEFT CLICK
        if menu_dict["option_menu"].active:
            for slider in menu_dict["option_menu"].slider_list:
                if slider.box_rect.collidepoint(x,y):
                    slider.circle_pos[0] = x
        elif menu_dict["start_menu"].active:
            for slider in menu_dict["start_menu"].slider_list:
                if slider.box_rect.collidepoint(x,y):
                    slider.circle_pos[0] = x
        if game_screen.active:
            #Go past the first 6 pins that should remain static
            for pin in game_screen.guess_box.color_pins_area.pin_list[6:]:
                if game_screen.guess_box.rect.collidepoint(x,y):
                    pin.rect_big.center, pin.rect.center = (x,y),(x,y)
                    #Print color
                    #print([k for k, v in settings.colors.items() if v == pin.color][0])
    else:
        if len(game_screen.guess_box.color_pins_area.pin_list) > 6:
            do_break = False
            for guess_pin in game_screen.guess_box.guess_pin_list:
                if guess_pin.rect.collidepoint(game_screen.guess_box.color_pins_area.pin_list[-1].rect.center):
                    guess_pin.color = game_screen.guess_box.color_pins_area.pin_list[-1].color
                else:
                    for pin in game_screen.guess_box.color_pins_area.pin_list[:6]:
                        if pin.rect.collidepoint(game_screen.guess_box.color_pins_area.pin_list[-1].rect.center):
                            if guess_pin.color == guess_pin.settings.guess_pin_color_inactive or guess_pin.color == guess_pin.settings.guess_pin_color_selected:
                                guess_pin.color = pin.color
                                do_break = True
                if do_break:
                    break

            game_screen.guess_box.color_pins_area.pin_list.pop()

def create_draggable_pin(settings,screen,pos,color):
    return Pin(settings,screen,pos,color,settings.medium_pin_radius)

def convert_ticks_to_time(ticks):
    time_list= []
    
    counting_minutes = str(int(ticks/60000)).zfill(2)
    counting_seconds = str(int((ticks%60000)/1000)).zfill(2)

    time_list.append(counting_minutes)
    time_list.append(counting_seconds)
    return time_list

def get_surf_darken_screen(screen, settings):
    darken_surf = pygame.Surface((settings.screen_width, settings.screen_height), pygame.SRCALPHA)
    darken_surf.set_alpha(100)
    pygame.draw.rect(darken_surf,(0,0,0),settings.rect)
    return darken_surf

"""ADD ANIMATONS"""