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