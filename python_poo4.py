import math
class Circle(object):

    def __init__(self):
        self.radio = float()
        self.resultado = float()
        self.signal = True

    def obtener_radio(self):

        while self.signal:
            try:

                self.radio = float(input("Inserte el valor del radio: "))
                self.signal = False
                
            except ValueError:
                print("Inserte un número valido")

    def calcular_area(self):
        
        self.resultado = (math.pi * self.radio ** 2)

    def imprimit_resultado(self):

        return print("El área del circulo es: {}".format(round(self.resultado, 2)))

    
circulo = Circle()
circulo.obtener_radio()
circulo.calcular_area()
circulo.imprimit_resultado()
