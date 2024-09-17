import numpy as np

def logica_x (tabuleiro = np.empty((3, 3), dtype=str)):
    for i in range(3):
        #Verifica as colunas
        if np.all(tabuleiro[:, i] == 'X'):
            print('X ganhou')
            print(tabuleiro)
            return True
        
        #Verifica as linhas
        if np.all(tabuleiro[i, :] == 'X'):
            print('X ganhou')
            print(tabuleiro)
            return True
        
    #Verifica as diagonais 
    if np.all(np.diag(tabuleiro) == 'X'):
        print('X ganhou')
        print(tabuleiro)
        return True
        
    if np.all(np.diag(np.fliplr(tabuleiro)) == 'X'):
        print('X ganhou')
        print(tabuleiro)
        return True






def logica_o (tabuleiro = np.empty((3, 3), dtype=str)):
    
    for i in range(3):
        #Verifica as colunas
        if np.all(tabuleiro[:, i] == 'O'):
            print('O ganhou')
            print(tabuleiro)
            return True
        
        #Verifica as linhas
        if np.all(tabuleiro[i, :] == 'O'):
            print('O ganhou')
            print(tabuleiro)
            return True

    #Verifica as diagonais 
    if np.all(np.diag(tabuleiro) == 'O'):
        print('O ganhou')
        print(tabuleiro)
        return True
        
    if np.all(np.diag(np.fliplr(tabuleiro)) == 'O'):
        print('O ganhou')
        print(tabuleiro)
        return True   