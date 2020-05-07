class Calculo(object):
    def __init__(self):
        self.numeros = []
        self.sumatoria = 0
        while True:
            numero = int(input("Ingrese un número: "))
            if numero != 0:
                self.numeros.append(numero)
            else:
                break

    def suma(self):
        for numero in self.numeros:
            self.sumatoria += numero
    
    def visualizar_suma(self):

        return print("La suma es: {}".format(self.sumatoria))

    
class Promedio(Calculo):

    def __init__(self):
        Calculo.__init__(self)

    def calc_promedio(self):

        promedio = self.sumatoria // len(self.numeros)

        return print("El promedio es: {}".format(promedio))


objeto = Promedio()
objeto.suma()
objeto.visualizar_suma()
objeto.calc_promedio()