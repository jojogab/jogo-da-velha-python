import numpy as np
from AreaDoJogo.Area import area


def checkvalid(linha, coluna):
    if 0 >= linha and linha > 3 or 0 >= coluna and coluna > 3:
        print('Número inválido, perdeu um round')
    else:
        print(area)

def checkvictoryp1(jogador):
    for i in range(3):
        if np.all(area[i, :] == 'X') or np.all(area[:, i] == 'X'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

        if np.all(np.diag(area) == 'X'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

        if np.all(np.diag(np.fliplr(area)) == 'X'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

    return False

def checkvictoryp2(jogador):
    for i in range(3):
        if np.all(area[i, :] == 'O') or np.all(area[:, i] == 'O'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

        if np.all(area[i, :] == 'O'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

        if np.all(np.diag(area) == 'O'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

        if np.all(np.diag(np.fliplr(area)) == 'O'):
            print(f'{jogador} ganhou!')
            print(area)
            arq_resultado = open('arquivo.txt', 'w')
            arq_resultado.write(f'{jogador} ganhou!\n')
            arq_resultado.write(f'{area}\n')
            arq_resultado.close()
            return True

    return False

def checkdraw():
    return not np.any(area == ' ')