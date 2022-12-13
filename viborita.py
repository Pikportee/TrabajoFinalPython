import turtle as tr
import time
import random

class vibora:
    def __init__(self):
        pass
    def viborita():
        posponer = 0.1

        score = 0
        highScore = 0

        wn = tr.Screen()
        wn.title("Viborita")
        wn.bgcolor("black")
        wn.setup(width=800, height=800)
        wn.tracer(0)

        vibora = tr.Turtle()
        vibora.speed(0)
        vibora.shape("square")
        vibora.color("white")
        vibora.penup()
        vibora.goto(0, 0)
        vibora.direction = "stop"

        #food
        food = tr.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        x = random.randint(-300,300)
        y = random.randint(-300, 300)
        food.goto(x,y)

        #cuerpo
        cuerpo = []

        #puntuacion
        puntuar = tr.Turtle()
        puntuar.speed(0)
        puntuar.color("white")
        puntuar.penup()
        puntuar.hideturtle()
        puntuar.goto(0,350)
        puntuar.write("Score: 0         High Score: 0" , align="center", font= ("Courier", 25, "normal"))

        #movimiento
        def up():
            vibora.direction = "up"
        def down():
            vibora.direction = "down"
        def left():
            vibora.direction = "left"
        def rigth():
            vibora.direction = "right"


        def mov():
            if vibora.direction == "up":
                y = vibora.ycor()
                vibora.sety(y + 20)

            if vibora.direction == "down":
                y = vibora.ycor()
                vibora.sety(y - 20)

            if vibora.direction == "left":
                x = vibora.xcor()
                vibora.setx(x - 20)

            if vibora.direction == "right":
                x = vibora.xcor()
                vibora.setx(x + 20)

        #teclado
        wn.listen()
        wn.onkeypress(up, "w")
        wn.onkeypress(down, "s")
        wn.onkeypress(left, "a")
        wn.onkeypress(rigth, "d")


            

        while True:
            wn.update()

            #colision borde
            if vibora.xcor() > 380 or vibora.xcor() < -380 or vibora.ycor() > 380 or vibora.ycor() < -380:
                time.sleep(1)
                vibora.goto(0,0)
                vibora.direction= "stop"
                x = random.randint(-300,300)
                y = random.randint(-300, 300)
                food.goto(x,y)

                for cuerpos in cuerpo:
                    cuerpos.goto(1000,1000)

                cuerpo.clear()

                #reset marcador
                score = 0
                puntuar.clear()
                puntuar.write("Score: {}         High Score: {}".format(score,highScore), align="center", font= ("Courier", 25, "normal"))

                gameOver = tr.Turtle()
                gameOver.speed(0)
                gameOver.color("red")
                gameOver.penup()
                gameOver.hideturtle()
                gameOver.goto(0,0)
                gameOver.write("Game Over" , align="center", font= ("Courier", 80, "normal"))
                time.sleep(1.5)
                gameOver.clear()

            #colicion cuerpo
            for cuerpos in cuerpo:
                if cuerpos.distance(vibora) < 20:
                    time.sleep(1)
                    vibora.goto(0,0)
                    vibora.direction = "stop"

                    for cuerpos in cuerpo:
                        cuerpos.goto(1000,1000)

                    cuerpo.clear()
                    score = 0
                    puntuar.clear()
                    puntuar.write("Score: {}         High Score: {}".format(score,      highScore), align="center", font= ("Courier", 25, "normal"))

                    gameOver = tr.Turtle()
                    gameOver.speed(0)
                    gameOver.color("red")
                    gameOver.penup()
                    gameOver.hideturtle()
                    gameOver.goto(0,0)
                    gameOver.write("Game Over" , align="center", font= ("Courier", 80, "normal"))
                    time.sleep(1.5)
                    gameOver.clear()

                
            if vibora.distance(food) < 15:
                x = random.randint(-300,300)
                y = random.randint(-300, 300)
                food.goto(x,y)

                nuevo_cuerpo = tr.Turtle()
                nuevo_cuerpo.speed(0)
                nuevo_cuerpo.shape("square")
                nuevo_cuerpo.color("grey")
                nuevo_cuerpo.penup()
                cuerpo.append(nuevo_cuerpo)

                #sumar marcador
                score += 1
                if score > highScore:
                    highScore = score
                
                puntuar.clear()
                puntuar.write("Score: {}         High Score: {}".format(score,highScore), align="center", font= ("Courier", 25, "normal"))

            #movimiento del cuerpo
            totalCuerpo = len(cuerpo)
            for index in range(totalCuerpo -1, 0, -1):
                x = cuerpo[index -1].xcor()
                y = cuerpo[index -1].ycor()
                cuerpo[index].goto(x,y)
            
            if totalCuerpo > 0:
                x = vibora.xcor()
                y = vibora.ycor()
                cuerpo[0].goto(x,y)
                
            mov()
            time.sleep(posponer)

