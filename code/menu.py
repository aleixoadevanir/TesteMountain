#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_LARANJA, MENU_OPCOES, COLOR_BRANCO, COLOR_AMARELO


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_opcoes = 0
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_LARANJA, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_LARANJA, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPCOES)):
                if i == menu_opcoes:
                    self.menu_text(20, MENU_OPCOES[i], COLOR_AMARELO, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPCOES[i], COLOR_BRANCO, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_opcoes < len(MENU_OPCOES) - 1:
                            menu_opcoes += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_opcoes > 0:
                            menu_opcoes -= 1
                        else:
                            menu_opcoes = len(MENU_OPCOES) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPCOES[menu_opcoes]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)