from random import randint
import sys
import pygame

from guess_area import Guesspincolor

<<<<<<< HEAD
def update_screen(settings, screen, main_menu, option_menu):
    
    screen.blit(settings.bg, settings.rect)
    
    if main_menu.active:
        main_menu.blitme()
    elif option_menu.active:
        option_menu.blitme()
    
    dict = {
        1: [230, 230, 250],
        2: [255, 165, 0],
        3: [233, 150, 122],
        4: [176, 224, 230],
        5: [127, 255, 0],
        6: [255, 255, 51]
    }
    color = dict[randint(1,6)]
    pygame.draw.circle(screen,color,(10,10),radius=50)
    pass
=======

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
        game_screen.guess_box.blitme()
        if game_screen.game_board.new_guess : game_screen.game_board.new_guess.blitme()
        for pin in game_screen.guess_box.guess_pin_list:
            pin.blitme()
        game_screen.guess_box.color_pins_area.blitme()
>>>>>>> 154f93c11eebd5b2a55f619d31e5d76bd8182103
    
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
    
    #display the last drawn screen
    pygame.display.flip()
    
<<<<<<< HEAD
def check_events(settings, screen, main_menu, option_menu):
=======
def check_events(settings, screen, menu_dict, game_screen):
>>>>>>> 154f93c11eebd5b2a55f619d31e5d76bd8182103
    for event in pygame.event.get():
        #If event is quit then quit
        if event.type == pygame.QUIT:
            sys.exit
        #Here go all the other event checks
        #FOR CLICKING THE MOUSE (ONE TIME EVENT)
        elif event.type == pygame.MOUSEBUTTONDOWN:
<<<<<<< HEAD
            check_mouse_click_events(event, settings,screen, main_menu, option_menu)
            
def check_keydown_events(event, settings, screen):
    pass

def check_mouse_click_events(event, settings,screen, main_menu, option_menu):
=======
            check_mouse_down_events(event, settings,screen, menu_dict, game_screen)
        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouse_up_events(event, settings,screen, menu_dict, game_screen)
    
    #FOR HOLDING DOWN THE MOUSE
    if pygame.mouse.get_pressed()[0]:
        check_mouse_hold_events(settings,screen,menu_dict, game_screen, hold=True)

            

def check_mouse_down_events(event, settings,screen, menu_dict, game_screen):
    #Function for mouse clicks
>>>>>>> 154f93c11eebd5b2a55f619d31e5d76bd8182103
    #Get the x and y location of where has been clicked
    x, y = event.pos
    
    if event.button == 1: #LEFT CLICK
<<<<<<< HEAD
        if main_menu.active:
            for button in main_menu.button_list:
=======
        #MENU INTERACTIONS
        if menu_dict["main_menu"].active:
            for button in menu_dict["main_menu"].button_list:
>>>>>>> 154f93c11eebd5b2a55f619d31e5d76bd8182103
                if button.rect.collidepoint(x,y):
                    main_menu.clicky_wicky_uwu(button)
                    break
        elif option_menu.active:
            for button in option_menu.button_list:
                if button.rect.collidepoint(x,y):
<<<<<<< HEAD
                    option_menu.clicky_wicky_uwu(button)
                    break
=======
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
>>>>>>> 154f93c11eebd5b2a55f619d31e5d76bd8182103
