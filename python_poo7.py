class ZeroValueException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return "ZeroValueException: {}".format(self.mensaje)

class Farenheit(object):

    def __init__(self):
        self.celsius = 0

    def asingment_value_celsius(self):

        while True:
            try:
                self.celsius = int(input("Insert the celsius grades: "))
                if self.celsius == 0:                                                                                                                                                                      
                    raise ZeroValueException('Inserte un valor mayor a 0')
                else:
                    break

            except ZeroValueException as e:
                print(e)

            except ValueError as e:
                print("No se puede introducir texto, ",e)

    def calcular_grados(self):

        return print("Los grados son: {}".format(1.8*(self.celsius + 32)))

grados = Farenheit()
grados.asingment_value_celsius()
grados.calcular_grados()


