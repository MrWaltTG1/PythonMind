
import sys
import pygame

from guess_area import Guesspincolor


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
        game_screen.draw_timer()
        game_screen.guess_box.blitme()
        for guess in game_screen.game_board.total_guesses:
            guess.blitme()
        for pin in game_screen.guess_box.guess_pin_list:
            pin.blitme()
        game_screen.guess_box.color_pins_area.blitme()
        if game_screen.won:
            game_screen.retry_button.draw_button()
    
    """dict = {
        1: [230, 230, 250],
        2: [255, 165, 0],
        3: [233, 150, 122],
        4: [176, 224, 230],
        5: [127, 255, 0],
        6: [255, 255, 51]
    }
    color = dict[randint(1,6)]
    pygame.draw.circle(screen,color,(10,10),radius=50)
    pass"""
    
    """ mylist = [[230, 230, 250],[255, 165, 0], [233, 150, 122]]
    
    color_list = random.choices(mylist, k=4)
    for color in color_list:
        pygame.draw.circle(screen,color,(10,10),radius=50)
    """
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
                    menu_dict["main_menu"].clicky_wicky_uwu(button)
                    break
        elif menu_dict["option_menu"].active:
            for button in menu_dict["option_menu"].button_list:
                if button.rect.collidepoint(x,y):
                    menu_dict["option_menu"].clicky_wicky_uwu(button)
                    break
            for slider in menu_dict["option_menu"].slider_list:
                if slider.box_rect.collidepoint(x,y):
                    slider.circle_pos[0] = x
        elif menu_dict["start_menu"].active:
            for button in menu_dict["start_menu"].button_list:
                if button.rect.collidepoint(x,y):
                    menu_dict["start_menu"].clicky_wicky_uwu(button)
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
                    pin.rect.center = (x,y)
                    #Print color
                    #print([k for k, v in settings.colors.items() if v == new_pin.color][0])
    else:
        if len(game_screen.guess_box.color_pins_area.pin_list) > 6:
            for guess_pin in game_screen.guess_box.guess_pin_list:
                #for pin in game_screen.guess_box.color_pins_area.pin_list[5:]:
                    if guess_pin.rect.collidepoint(game_screen.guess_box.color_pins_area.pin_list[-1].rect.center):
                            guess_pin.color = game_screen.guess_box.color_pins_area.pin_list[-1].color
            game_screen.guess_box.color_pins_area.pin_list.pop()

def create_draggable_pin(settings,screen,pos,color):
    return Guesspincolor(settings,screen,pos,color)

def convert_ticks_to_time(ticks):
    time_list= []
    
    seconds = ticks / 1000
    minutes = ticks / 60000
    #print(seconds)
    #print(minutes)
    
    counting_minutes = str(int(ticks/60000)).zfill(2)
    counting_seconds = str(int((ticks%60000)/1000)).zfill(2)
    counting_millisecond = str(int(ticks%1000)).zfill(2)
    
    time_list.append(counting_minutes)
    time_list.append(counting_seconds)
    time_list.append(counting_millisecond)
    return time_list