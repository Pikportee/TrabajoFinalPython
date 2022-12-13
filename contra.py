import random 

class contraseña:
    def __init__(self):
        pass

    def contraseña(self):
        long = int(input("¿De cuantos caracteres quiere su contraseña?\n")) 

        minus = "abcdefghijklmnñopqrstuvwxyz" 
        mayus = minus.upper() 
        numeros = "0123456789" 
        simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%=" 

        base = minus+mayus+numeros+simbolos 
        muestra = random.sample(base, long)
        contraseña = "".join(muestra) 
        print(contraseña) 

    