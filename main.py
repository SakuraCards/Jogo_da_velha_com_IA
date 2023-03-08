from Jogo_da_velha import criarTela, FazMovimentos, getInputValido, \
                            printTela, verificarGanhador, verificarMovimento 
from minimax import movimentoIA

jogador = 0 # jogador 1
Tela = criarTela()
ganhador = verificarGanhador(Tela)
while (not ganhador):
    printTela(Tela)
    print ("===================")
    if(jogador == 0):
        i,j = movimentoIA(Tela, jogador)
    else: 
        i = getInputValido("Digite a linha: ")
        
        j = getInputValido("Digite a coluna: ")

    if(verificarMovimento(Tela, i, j)):
        FazMovimentos(Tela, i, j, jogador)
        jogador = (jogador + 1)%2 
    else:
        print("A posição informada já está ocupada") 

    ganhador = verificarGanhador(Tela)    
    

print ("===================")
printTela(Tela)
print("Ganhador = ", ganhador)
print ("===================")
            

