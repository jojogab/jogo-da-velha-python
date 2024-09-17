import numpy as np

area = np.full((3,3), '', dtype=str)

def jogadap1(linha, coluna, valor):
    if area[linha, coluna] == '':
        area[linha, coluna] = valor
    else:
        print('A linha já está em uso, perdeu um round')

def jogadap2(linha, coluna, valor):
    if area[linha, coluna] == '':
        area[linha, coluna] = valor
    else:
        print('A linha já está em uso, perdeu um round')



