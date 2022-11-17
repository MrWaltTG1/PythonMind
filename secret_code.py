import random
import pygame

from elements import Pin


class SecretCode():
    def __init__(self, settings, screen) -> None:
        self.settings = settings
        self.screen = screen
        self.original_surf = self.settings.shine_image
        self.hover = False
        pos = (0, 0)
        size = (400, 100)
        self.bbox_rect = pygame.rect.Rect(pos, size)
        self.bbox_rect.midtop = (self.settings.screen_width / 3, 20)
        self.filled = 0

        self.create_pins()
        self.text_box()

    def update(self, won):
        self.won = won
        if won:
            self.filled = 2
        self.code_list = []
        for pin in self.pin_list:
            self.code_list.append(pin.color)

        x, y = pygame.mouse.get_pos()
        if self.bbox_rect.collidepoint(x, y):
            self.hover = True
        else:
            self.hover = False

    def create_pins(self):
        self.colorlist = list(self.settings.colors.values())
        self.pin_list, self.hidden_pin_list, self.q_list = [], [], []
        pin_pos = self.bbox_rect.midleft
        i = 0
        while i < self.settings.code_length:
            random_color = random.choice(self.colorlist)
            while random_color == self.settings.colors["brown"]:
                random_color = random.choice(self.colorlist)
            if self.settings.difficulty == 1:
                self.colorlist.remove(random_color)
            pin_pos = (pin_pos[0] + 80, pin_pos[1])
            new_pin = Pin(self.settings, self.screen, pin_pos,
                          random_color, self.settings.big_pin_radius)
            new_hidden_pin = Pin(self.settings, self.screen, pin_pos,
                                 self.settings.guess_pin_color_inactive, self.settings.big_pin_radius)
            self.pin_list.append(new_pin)
            self.hidden_pin_list.append(new_hidden_pin)
            self.create_question_mark(pin_pos)
            i += 1

    def create_question_mark(self, pos):
        self.font = pygame.font.SysFont(
            self.settings.font_type, self.settings.font_size)
        self.msg_image = self.font.render(
            "?", True, self.settings.hud_colors["white"])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = pos
        self.q_list.append((self.msg_image, self.msg_image_rect))

    def text_box(self):
        msg = "P y t h o n M i n d"
        self.font = pygame.font.SysFont(
            self.settings.font_type, self.settings.font_size)
        self.msg_image = self.font.render(
            msg, True, self.settings.hud_colors["white"])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.bbox_rect.center
        self.msg_image_rect.centery += 30

    def blitme(self):
        if self.hover and self.filled == 0:
            pygame.draw.rect(
                self.screen, self.settings.hud_colors['red'], self.bbox_rect, width=self.filled)
            for pin in self.hidden_pin_list:
                pin.blitme()
            for q in self.q_list:
                self.screen.blit(q[0], q[1])
        else:
            for pin in self.pin_list:
                pin.blitme()
            pygame.draw.rect(
                self.screen, self.settings.hud_colors['red'], self.bbox_rect, width=self.filled)
            if self.filled == 0:
                self.screen.blit(self.msg_image, self.msg_image_rect)
