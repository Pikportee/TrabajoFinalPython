import Dados
import numAleatorio
import mathplotlib
import contra
import viborita
import PiedraPapelTijera2



print("Buenos días, entro al trabajo de Agustin Violante para el curso de Python de DigitalMind, se trata de varios juegos en los que puedes participar, pero primero...")
nombre = input("¿Cuál es tu nombre?\n")
num_juego = int(input(f"Bienvenido {nombre} cual juego es el que quieres participar?\n-1 Tirar los dados \n-2 Elegir un numero aleatorio \n-3 Piedra papel y tijeras \n-4 Armar una contraseña \n-5 Grafico con varios números \n-6 El juego de la viborita \n"))

if num_juego == 1:
    juego = Dados.dado()
    juego.tirarDados()

if num_juego == 2:
    juego = numAleatorio.num_Aleatorio()
    juego.numAl()

if num_juego == 3:
    juego = PiedraPapelTijera2.piedra_papel_tijera()
    juego.jugar()
    
if num_juego == 4:
    juego = contra.contraseña()
    juego.contraseña()

if num_juego == 5:
    juego = mathplotlib.grafico()
    juego.cuenta()

if num_juego == 6:
    juego = viborita.vibora
    juego.viborita()




