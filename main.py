from AreaDoJogo.Area import jogadap1, jogadap2
from Checks.check import checkvalid, checkvictoryp1, checkvictoryp2, checkdraw

print("""### JOGO DA VELHA ###""")

jogador1 = str(input("Defina o nome do jogador 1: "))
jogador2 = str(input("Defina o nome do jogador 2: "))

victory = False

print('''  0   1  2
0 ['' '' '']                  
1 ['' '' '']
2 ['' '' '']
''')

while True:

    print(f"Turno do {jogador1}")
    linha = int(input("Defina o valor da linha: "))
    coluna = int(input("Defina o valor da coluna: "))
    valor = 'X'

    jogadap1(linha, coluna, valor)
    checkvalid(linha, coluna)
    checkdraw()
    checkvictoryp1(jogador1)

    print(f"Turno do {jogador2}")
    linha = int(input("Defina o valor da linha: "))
    coluna = int(input("Defina o valor da coluna: "))
    valor = 'O'

    jogadap2(linha, coluna, valor)
    checkvalid(linha, coluna)
    checkdraw()
    checkvictoryp2(jogador2)
