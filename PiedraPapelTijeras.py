from cmath import pi
import random

class piedra_papel_tijera:
    def __init__(self):
        pass
    def jugar(self):
        usuario1= input('Escoje una opcion. "pi" para piedra. "pa" para papel. "ti" para tijera.\n').lower()
        compu= random.choice(['pi', 'pa', 'ti'])

        if usuario1 == compu:
            return '¡Han empatado!'

        if ganaste(usuario1, compu):
            return '¡Has ganado!'

        return '¡Lo siento, has perdido!'

class ganador:
    def __init__(self):
        pass
def ganaste(jugador, oponente, self):
    if ((jugador == 'pi' and oponente == 'ti')
    or (jugador == 'ti' and oponente == 'pa')
    or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False





if __name__ == '__main__':
    piedra_papel_tijera()
