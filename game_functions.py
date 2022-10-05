from random import randint
import sys
import pygame


def update_screen(settings, screen, menu_dict, game_screen):
    
    screen.blit(settings.bg, settings.rect)
    
    if menu_dict["main_menu"].active:
        menu_dict["main_menu"].blitme()
    elif menu_dict["option_menu"].active:
        menu_dict["option_menu"].blitme()
    elif menu_dict["start_menu"].active:
        menu_dict["start_menu"].blitme()
    else:
        game_screen.update()
    
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
    
    pygame.display.flip()
    
def check_events(settings, screen, menu_dict):
    for event in pygame.event.get():
        #If event is quit then quit
        if event.type == pygame.QUIT:
            sys.exit()
        #Here go all the other event checks
        #FOR CLICKING THE MOUSE (ONE TIME EVENT)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click_events(event, settings,screen, menu_dict)
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
    
    #FOR HOLDING DOWN THE MOUSE
    if pygame.mouse.get_pressed()[0]:
        check_mouse_hold_events(settings,screen,menu_dict)
            

def check_mouse_click_events(event, settings,screen, menu_dict):
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
        #END OF MENU INTERACTIONS

def check_mouse_hold_events(settings,screen,menu_dict, hold = False):
    #Function for holding down the mouse button
    x,y = pygame.mouse.get_pos()
    
    #if event.button == 1: #LEFT CLICK
    if menu_dict["option_menu"].active:
        for slider in menu_dict["option_menu"].slider_list:
            if slider.box_rect.collidepoint(x,y):
                hold = True
                slider.circle_pos[0] = x
            if hold:
                slider.circle_pos[0] = x