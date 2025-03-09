#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
class Game:
    def __init__(self):
        self.window = None

def run(self, ):

    print('Setup Start')

pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup End')
print('Loop Setup')
while True:
    ## Checar todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  ##Fechar Janela
            quit()  ## fechar jogo
