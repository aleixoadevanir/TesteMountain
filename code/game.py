#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.level import Level
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPCOES

# CONSTANTES
MENU_JOGAR_OPCOES = [MENU_OPCOES[0], MENU_OPCOES[1], MENU_OPCOES[2]]  # Opções de jogo


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            selected_option = menu.run()

            if selected_option in MENU_JOGAR_OPCOES:
                self.start_level(selected_option)
            elif selected_option == MENU_OPCOES[4]:
                pygame.quit()
                quit()

    def start_level(self, game_mode):
        """Inicializa e executa um nível do jogo."""
        level = Level(self.window, "Level1Bg", game_mode)
        level_result = level.run()
        return level_result

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPCOES [0], MENU_OPCOES [1], MENU_OPCOES [2]]:
                level = Level(self.window,"Level1Bg", menu_return)
                level_return = level.run

            elif menu_return == MENU_OPCOES [4]:
                pygame.quit()
                quit()
            else:
                pass