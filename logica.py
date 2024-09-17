import numpy as np

def logica_x (tabuleiro = np.empty((3, 3), dtype=str)):
        # ifs das colunas X
    if tabuleiro[0, 0] == tabuleiro[1, 0] == tabuleiro [2, 0] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 1] == tabuleiro[1, 1] == tabuleiro [2, 1] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 2] == tabuleiro[1, 2] == tabuleiro [2, 2] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    


    
    # ifs das linhas X
    if tabuleiro[0, 0] == tabuleiro[0, 1] == tabuleiro [0, 2] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[1, 0] == tabuleiro[1, 1] == tabuleiro [1, 2] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[2, 0] == tabuleiro[2, 1] == tabuleiro [2, 2] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    

    # ifs das diagonais X

    if tabuleiro[0, 0] == tabuleiro[1, 1] == tabuleiro [2, 2] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 2] == tabuleiro[1, 1] == tabuleiro [2, 0] == 'X':
        print('X ganhou')
        print(tabuleiro)
        return True;






def logica_o (tabuleiro = np.empty((3, 3), dtype=str)):
    
    # ifs das colunas O
    if tabuleiro[0, 0] == tabuleiro[1, 0] == tabuleiro [2, 0] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 1] == tabuleiro[1, 1] == tabuleiro [2, 1] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 2] == tabuleiro[1, 2] == tabuleiro [2, 2] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    


    
    # ifs das linhas O
    if tabuleiro[0, 0] == tabuleiro[0, 1] == tabuleiro [0, 2] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[1, 0] == tabuleiro[1, 1] == tabuleiro [1, 2] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[2, 0] == tabuleiro[2, 1] == tabuleiro [2, 2] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    

    # ifs das diagonais O
    if tabuleiro[0, 0] == tabuleiro[1, 1] == tabuleiro [2, 2] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;
    
    elif tabuleiro[0, 2] == tabuleiro[1, 1] == tabuleiro [2, 0] == 'O':
        print('O ganhou')
        print(tabuleiro)
        return True;