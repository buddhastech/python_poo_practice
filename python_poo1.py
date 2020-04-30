# Problema: Leer los lados de un triángulo, calcular la hipotenusa y
# presentar el resultado

import math # import of math module

class Triangle(object):
    def __init__(self, a1, a2):
        self.a1 = a1; self.a2 = a2 # atributtes of triangle class

    def calculate_hypotenuse(self):
        self.hypotenuse = math.sqrt(self.a1 ** 2 + self.a2 ** 2)
        # Calculate the hypotenuse of the triangle object

        return print("The Hypotenuse is: {}".format(int(self.hypotenuse)))
        # return the result of the calculation

#triangle = Triangle(32, 24)  Instance of Triangle class
#triangle.calculate_hypotenuse()  Use the method calculate_hypotenuse with the object

class Triangulo(object):
    
    def __init__(self):
        self.cat1 = 0
        self.cat2 = 0

    def asignar_valores(self):

        self.cat1 = float(input("Valor de cateto 1: "))
        self.cat2 = float(input("Valor de cateto 2: "))

    def calcular_hipotenusa(self):
        
        return print("La hipotenusa es: {}".format(math.sqrt(self.cat1 **2 + self.cat2 ** 2)))
    
triangulo = Triangulo()
triangulo.asignar_valores()
triangulo.calcular_hipotenusa()
