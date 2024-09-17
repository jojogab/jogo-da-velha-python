import os
import numpy as np
import logica as lgc
import regrasJogada as rj

tabuleiro = np.empty((3, 3), dtype=str)

nomeJogador1 = input('Digite o nome do primeiro jogador: ')
nomeJogador2 = input('Digite o nome do segundo jogador: ')

posicaoX = int(input('Digite a posição X para sua jogada: '))
posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
jogadaJ1 = input('Digite sua jogada: ').upper()
    
rj.verificaJogada(tabuleiro, jogadaJ1, posicaoX, posicaoY, nomeJogador1, nomeJogador2)
    
posicaoX = int(input('Digite a posição X para sua jogada: '))
posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
jogadaJ2 = input('Digite sua jogada: ').upper()

rj.verificaJogada(tabuleiro, jogadaJ2, posicaoX, posicaoY, nomeJogador1, nomeJogador2)

while True:
    print(tabuleiro)

    posicaoX = int(input('Digite a posição X para sua jogada: '))
    posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
    jogadaJ1 = input('Digite sua jogada: ').upper()
    
    rj.verificaJogada(tabuleiro, jogadaJ1, posicaoX, posicaoY, nomeJogador1, nomeJogador2)
    
    posicaoX = int(input('Digite a posição X para sua jogada: '))
    posicaoY = int(input('Digite a posição Y para sua jogada: '))
    
    jogadaJ2 = input('Digite sua jogada: ').upper()
    
    rj.verificaJogada(tabuleiro, jogadaJ2, posicaoX, posicaoY, nomeJogador1, nomeJogador2)

    jogadaJ1 = ''
    jogadaJ2 = ''
    
    os.system('cls' if os.name == 'nt' else 'clear')

    
