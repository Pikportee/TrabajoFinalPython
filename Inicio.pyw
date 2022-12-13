import Dados
import numAleatorio
import PiedraPapelTijeras
import mathplotlib
import contra
import viborita



print("Buenos días, entro al trabajo de Agustin Violante para el curso de Python de DigitalMind, se trata de varios juegos en los que puedes participar, pero primero...")
nombre = input("¿Cuál es tu nombre?\n")
num_juego = int(input(f"Bienvenido {nombre} cual juego es el que quieres participar?\n-1 \n-2 \n-3 \n-4 \n-5 \n-6 \n"))

if num_juego == 1:
    juego = Dados.dado()
    juego.tirarDados()

if num_juego == 2:
    juego = numAleatorio.num_Aleatorio()
    juego.numAl()

if num_juego == 3:
    juego = PiedraPapelTijeras.piedra_papel_tijera()
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




