import pygame

class Pin():
    def __init__(self, settings, screen, pos, color, size, hidden = False) -> None:
        self.screen, self.settings, self.radius, self.pos, self.color,self.hidden = screen, settings, int(size/2),pos,color, hidden

        self.rect = pygame.draw.circle(self.screen, self.color, self.pos,self.radius)
        self.rect_big = pygame.draw.circle(self.screen,self.color,self.rect.center,self.radius + 2)
        self.original_shine_surf = self.settings.shine_image

    def blitme(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x,y):
            pygame.draw.circle(self.screen,self.color,self.rect.center,self.radius + 2)
            self.shine_surf = pygame.transform.scale(self.original_shine_surf, self.rect_big.size)
            self.screen.blit(self.shine_surf, self.rect_big)
            
        else:
            pygame.draw.circle(self.screen, self.color, self.rect.center,self.radius)
            self.shine_surf = pygame.transform.scale(self.original_shine_surf, self.rect.size)
            self.screen.blit(self.shine_surf, self.rect)
        if self.color == self.settings.guess_pin_color_inactive:
            if self.radius == self.settings.big_pin_radius / 2:
                pygame.draw.circle(self.screen,self.settings.hud_colors['black'],self.rect.center,self.radius - 4)
            else:
                pygame.draw.circle(self.screen,self.settings.hud_colors['black'],self.rect.center,self.radius - 2)
