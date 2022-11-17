import pygame
import game_functions as gf


class Button():

    def __init__(self, screen, settings, msg, pos, id):
        self.screen, self.settings, self.pos, self.msg = screen, settings, pos, msg
        self.border = 0
        self.textbox_list = None

        self.button_color = settings.button_color
        self.text_color = settings.text_color
        self.font_type = settings.font_type
        self.font_size = settings.font_size

        if id == "mm" or id == "gs":
            self.width, self.height = settings.mm_button_width, settings.mm_button_height

        elif id == "om":
            self.width, self.height = settings.om_button_width, settings.om_button_height

        elif id == "sm":
            self.width, self.height = settings.sm_button_width, settings.sm_button_height

        elif id == "gb":
            self.width, self.height = settings.gb_button_width, settings.gb_button_height
            self.font_type = settings.gb_font_type
            self.font_size = settings.gb_font_size
            self.border = 2
        elif id == "gb_2":
            self.width, self.height = settings.gb_button_width, settings.gb_button_height
            self.font_type = settings.gb_font_type
            self.font_size = settings.gb_font_size
            self.border = 0

        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = pos

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def create_text_box(self, text):
        size = (200, 40)
        pos = self.pos[0], self.pos[1] - 50
        self.textbox_list = gf.create_text_box(
            self.settings, pos, size, text, font_size=30, text_color=self.settings.hud_colors["white"])

    def blitme(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.button_color = self.settings.button_color_hover
        else:
            self.button_color = self.settings.button_color
        pygame.draw.rect(self.screen, self.button_color,
                         self.rect, border_radius=self.border)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        if self.textbox_list:
            pygame.draw.rect(self.screen, self.button_color,
                             self.textbox_list[0], width=-1)
            self.screen.blit(self.textbox_list[1][0], self.textbox_list[1][1])
