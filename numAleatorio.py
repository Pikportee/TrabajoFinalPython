from random import *

class num_Aleatorio:
    def __init__(self):
        pass
    def numAl(self):
        num_random = randint(1,100)
        intentos = 0

        playing = True

        print("Adivina el numero entre 1 y 100, tienes 7 intentos.")

        while playing:
            intentos +=1
            if intentos <= 7:
                numUsuario = int(input("¿Dime el numero que crees que es?"))
                if numUsuario == num_random:
                    print("PERFECTO, has acertado, tan solo has necesitado" , intentos, "intentos.")
                    playing = False
                elif numUsuario > num_random:
                    print("Es demasiado alto, proba uno mas bajo. Llevas" , intentos, "intentos.")
                elif numUsuario < num_random:
                    print("Es demasiado bajo, proba uno mas alto. Llevas" , intentos, "intentos.")
            else:
                print("Se te acabaron los intentos, has perdido :c")
                playing = False

if __name__ == '__main__':
    num_Aleatorio()
        

