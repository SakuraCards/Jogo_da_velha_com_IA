from Jogo_da_velha import branco, token, verificarGanhador

def movimentoIA(Tela, jogador):
    possibilidades = getPosicoes(Tela)
    MelhorValor = None 
    MelhorMovimento = None
    for possibilidade in possibilidades:
        Tela[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(Tela, jogador)
        Tela[possibilidade[0]][possibilidade[1]] = branco

        if(MelhorValor is None):
            MelhorValor = valor
            MelhorMovimento = possibilidade
        elif(jogador == 0):
            if(valor > MelhorValor):
                MelhorValor = valor
                MelhorMovimento = possibilidade
        elif(jogador == 1):
            if(valor < MelhorValor):
                MelhorValor = valor
                MelhorMovimento = possibilidade        
            

    
    return MelhorMovimento[0], MelhorMovimento[1]

def getPosicoes(Tela):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(Tela[i][j] == branco):
                posicoes.append([i, j])

    return posicoes 

score = {
    "EMPATE":0,
    "X":1,
    "O":-1
}               

def minimax(Tela, jogador):
    ganhador = verificarGanhador(Tela)
    if(verificarGanhador(Tela)):
        if(ganhador):
            return score[ganhador]

    jogador = (jogador + 1)%2 

    possibilidades = getPosicoes(Tela)
    MelhorValor = None 
    for possibilidade in possibilidades:
        Tela[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(Tela, jogador)
        Tela[possibilidade[0]][possibilidade[1]] = branco

        if(MelhorValor is None):
            MelhorValor = valor
        elif(jogador == 0):
            if(valor > MelhorValor):
                MelhorValor = valor
        elif(jogador == 1):
            if(valor < MelhorValor):
                MelhorValor = valor 

    return MelhorValor