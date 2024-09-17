import os
import numpy as np
import logica as lgc
import regrasJogada as rj

tabuleiro = np.empty((3, 3), dtype=str)

nomeJogador1 = input('Digite o nome do primeiro jogador: ')
nomeJogador2 = input('Digite o nome do segundo jogador: ')
jogadaJ1 = ''
jogadaJ2 = '' 
vitorias1 = 0
vitorias2 = 0

while True:
    print(tabuleiro)
    
    if rj.regraJogadaX(jogadaJ1):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogadaJ1
        print(tabuleiro)
        if lgc.logica_x(tabuleiro):
            os.system('cls' if os.name == 'nt' else 'clear')
            vitorias1 = vitorias1 + 1
            print(f'{nomeJogador1} ({vitorias1}) x {nomeJogador2} ({vitorias2}))')
            print(tabuleiro)
            break;
    
    if rj.regraJogadaO(jogadaJ2):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogadaJ2
        print(tabuleiro)
        if lgc.logica_o(tabuleiro):
            vitorias2 = vitorias2 + 1
            print(f'{nomeJogador1} ({vitorias1}) x {nomeJogador2} ({vitorias2}))')
            print(tabuleiro)
            break;
    
    posicaoX = int(input('Digite a posição X para sua jogada: '))
    posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
    jogadaJ1 = input('Digite sua jogada: ').upper()
    
    if rj.regraJogadaX(jogadaJ1):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogadaJ1
        print(tabuleiro)
        if lgc.logica_x(tabuleiro):
            vitorias1 = vitorias1 + 1
            print(f'{nomeJogador1} ({vitorias1}) x {nomeJogador2} ({vitorias2}))')
            print(tabuleiro)
            break;
    
    posicaoX = int(input('Digite a posição X para sua jogada: '))
    posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
    jogadaJ2 = input('Digite sua jogada: ').upper()
    
    if rj.regraJogadaO(jogadaJ2):
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro[posicaoX, posicaoY] = jogadaJ2
        print(tabuleiro)
        if lgc.logica_o(tabuleiro):
            vitorias2 = vitorias2 + 1
            print(f'{nomeJogador1} ({vitorias1}) x {nomeJogador2} ({vitorias2}))')
            print(tabuleiro)
            break;
    
    os.system('cls' if os.name == 'nt' else 'clear')

    
