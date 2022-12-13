import matplotlib.pyplot as plt

class grafico:
    def __init__(self):
        pass

    def cuenta(self):

        num1 = int(input("Decime el primer numero a graficar\n"))
        num2 = int(input("Decime el segundo numero a graficar\n"))
        num3 = int(input("Decime el tercer numero a graficar\n"))
        num4 = int(input("Decime el cuarto numero a graficar\n"))


        plt.plot([num1, num2, num3, num4])
        plt.title("Tu cuenta")
        plt.grid()
        plt.show()