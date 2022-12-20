
class piedra_papel_tijera:
    def __init__(self):
        pass
    def jugar(self):
        while True:
            print("Puedes elegir entre estas tres opciones")
            jugador = int(input("Jugador 1: 1=Piedra, 2=Papel o 3=Tijeras\n"))
            jugador2 = int(input("Jugador 2: 1=Piedra, 2=Papel o 3=Tijeras\n"))

            if jugador == 1 and jugador2 == 3:
                print("Gana el Jugador 1: Piedra gana a tijera")
            elif jugador == 2 and jugador2 == 1:
                print("Gana el Jugador 1: Papel gana a piedra")
            elif jugador == 3 and jugador2 == 2:
                print("Gana el Jugador 1: Tijera gana a papel")
            elif jugador2 == 1 and jugador == 3:
                print("Gana el Jugador 2: Piedra gana a Tijera")
            elif jugador2 == 2 and jugador == 1:
                print("Gana el Jugador 2: Papel gana a piedra")
            elif jugador2 == 3 and jugador == 2:
                print("Gana el Jugador 2: Tijera gana a Papel")
            else:
                print("ninguno es el ganador")

    