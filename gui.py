import pygame

from Jogo_da_velha import criarTela, FazMovimentos, getInputValido, \
                            printTela, verificarGanhador, verificarMovimento

from minimax import movimentoIA  

pygame.font.init()

def desenhar_tela(win, Tela):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1,3):
        pygame.draw.line(win,(82, 43, 71),(0,i*tamanho),(width, i  * tamanho),3)
        pygame.draw.line(win,(82, 43, 71),(i * tamanho, 0),(i * tamanho, height),3)

    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("Arial", 100)

            x = j * tamanho
            y = i * tamanho

            text = font.render(Tela[i][j], 1,(141, 170, 157))
            win.blit(text, ((x + 75), (y + 75)))
            
    
def redesenhar_janela(win, Tela):
    win.fill((251, 245, 243))
    desenhar_tela(win, Tela)

def main():
    win = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Jogo da Velha")

    Tela = criarTela()

    redesenhar_janela(win, Tela)
    pygame.display.update()

    jogador = 0 
    ganhador = verificarGanhador(Tela)

    while (not ganhador):
        printTela(Tela)
        if(jogador == 0):
            jogou = False
            while(not jogou):
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    elif(event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/200)
                        j = int(pos[0]/200)
                        jogou = True 
        else: 
           i,j = movimentoIA(Tela, jogador)

        if(verificarMovimento(Tela, i, j)):
           FazMovimentos(Tela, i, j, jogador)
           jogador = (jogador + 1)%2 
        
        ganhador = verificarGanhador(Tela)
        redesenhar_janela(win, Tela)
        pygame.display.update()
    
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return

main()