#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, MENU_OPCOES, COLOR_BRANCO


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load( './assets/MenuBg.png') ##carrega imagem de fundo do menu
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):
        ##Carrega musica do menu
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        ##loop da imagen do menu
        while True:

            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_tex(
                text_size=50,
                text="Mountain",
                text_color=(255, 128, 0),
                text_center_pos=((WIN_WIDTH / 2), 70)
            )
            self.menu_tex(
                text_size=50,
                text="Shooter",
                text_color=(255, 128, 0),
                text_center_pos=((WIN_WIDTH / 2), 120)
            )

            for i in range(len(MENU_OPCOES)):
                self.menu_tex(
                    text_size=20,
                    text=MENU_OPCOES[i],
                    text_color=COLOR_BRANCO,
                    text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i)
                )

            pygame.display.flip()

        ##Checar todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  ##Fechar Janela
                    quit()  ## fechar jogo

    def menu_tex(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color)
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
