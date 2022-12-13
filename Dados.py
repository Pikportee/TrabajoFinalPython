from random import *

valor1 = randint(1,6)
valor2 = randint(1,6)

class dado:
    def __init__(self):
        pass
    def tirarDados(self):
        print("tirando los dados")
        print(valor1)
        print(valor2)

if __name__ == '__main__':
    dado()