from random import randint
import sys
import pygame


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
    
    pygame.display.flip()
    
def check_events(settings, screen, main_menu, option_menu):
    for event in pygame.event.get():
        #If event is quit then quit
        if event.type == pygame.QUIT:
            sys.exit
        #Here go all the other event checks
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings, screen)
        elif event.type == pygame.KEYUP:
            check_keydown_events(event,settings,screen)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click_events(event, settings,screen, main_menu, option_menu)
            
def check_keydown_events(event, settings, screen):
    pass

def check_mouse_click_events(event, settings,screen, main_menu, option_menu):
    #Get the x and y location of where has been clicked
    x, y = event.pos
    
    if event.button == 1: #LEFT CLICK
        if main_menu.active:
            for button in main_menu.button_list:
                if button.rect.collidepoint(x,y):
                    main_menu.clicky_wicky_uwu(button)
                    break
        elif option_menu.active:
            for button in option_menu.button_list:
                if button.rect.collidepoint(x,y):
                    option_menu.clicky_wicky_uwu(button)
                    break