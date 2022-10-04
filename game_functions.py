import pygame


def update_screen(settings, screen):
    
    screen.blit(settings.bg, settings.rect)
    
    pygame.display.flip()