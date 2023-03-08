branco = " "
token = ["X", "O"]

def criarTela():
    Tela = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return Tela

def printTela(Tela): 
    for i in range(3):
        print("|".join(Tela[i]))
        if(i < 2):
            print("------")

def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <=3):
            return n - 1
        else:
            print("Numero precisa estar entre 1 e 3")
            return getInputValido(mensagem)           
    except:
        print("numero não é valido")
        getInputValido(mensagem) 

def verificarMovimento(Tela, i, j):
    if(Tela[i][j] == branco):
        return True
    else:
        return False  

def FazMovimentos(Tela, i, j, jogador):
    Tela[i][j] = token[jogador]  

def verificarGanhador(Tela):
    #LInhas
    for i in range(3):
        if(Tela[i][0] == Tela[i][1] and Tela[i][1] == Tela[i][2] and Tela[i][0] != branco):
            return Tela[i][0]

    # Coluna
    for i in range(3):
        if(Tela[0][i] == Tela[1][i] and Tela[1][i] == Tela[2][i] and Tela[0][i] != branco):
            return Tela[0][i]

    #Diagonal principal
    if(Tela[0][0] != branco and Tela[0][0] == Tela[1][1] and Tela[1][1] == Tela[2][2]):
        return Tela[0][0] 

    #Diagonal secundaria
    if(Tela[0][2] != branco and Tela[0][2] == Tela[1][1] and Tela[1][1] == Tela[2][0]):
        return Tela[0][2] 

    for i in range(3):
        for j in range(3):
            if(Tela[i][j] == branco):
                return False                       

    return "EMPATE"                                       
    