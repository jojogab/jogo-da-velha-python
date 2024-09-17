import os
import numpy as np
import logica as lgc

def regraJogadaX(jogada):
    if len(jogada) == 1 and jogada.upper() == 'X':
        return True
    else:
        return False

def regraJogadaO(jogada):
    if len(jogada) == 1 and jogada.upper() == 'O':
        return True
    else:
        return False

def verificaJogada(tabuleiro, jogada, posicaoX, posicaoY, jogador1, jogador2):
    if regraJogadaX(jogada):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogada
        print(tabuleiro)
        if lgc.logica_x(tabuleiro):
            os.system('cls' if os.name == 'nt' else 'clear')
            vitorias1 = vitorias1 + 1
            print(f'{jogador1} ({vitorias1}) x {jogador2} ({vitorias2}))')
            print(tabuleiro)
    else:
        print('Jogada invalida, tente novamente')

    if regraJogadaO(jogada):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogada
        print(tabuleiro)
        if lgc.logica_o(tabuleiro):
            os.system('cls' if os.name == 'nt' else 'clear')
            vitorias2 = vitorias2 + 1
            print(f'{jogador1} ({vitorias1}) x {jogador2} ({vitorias2}))')
            print(tabuleiro)
    else:
        print('Jogada invalida, tente novamente')