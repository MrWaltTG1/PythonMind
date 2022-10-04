import pygame


def update_screen(settings, screen, main_menu):
    
    screen.blit(settings.bg, settings.rect)
    
    main_menu.blitme()
    
    pygame.display.flip()