#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGT
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGT ))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
        pass
            ## Checar todos os eventos
            ##for event in pygame.event.get():
            ##    if event.type == pygame.QUIT:
            ##        pygame.quit()  ##Fechar Janela
            ##        quit()  ## fechar jogo
