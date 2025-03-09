import pygame

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
