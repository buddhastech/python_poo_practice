from exceptions.exceptions import ZeroValuesException


class Person(object):
    def __init__(self):
        self.nombre = ''
        self.horas_trabajadas = 0
        self.tarifa_hora = 1500
        self.deducciones = 0
        self.salario = 0

class Worker(Person):
    
    def asignar_valores(self):
        while True:
            try:
                self.nombre = "Mario"
                self.horas_trabajadas = int(input('Ingrese cuantas horas trabajó: '))
                self.deducciones = (self.horas_trabajadas * self.tarifa_hora) * 10 // 100
                
                if self.horas_trabajadas == 0:
                    raise ZeroValuesException('No debe ingresar 0')
                
                else:
                    break
                
            except ValueError as e:
                print("Debe ingresar un monto válido, Eror: {}".format(e))

            except ZeroValuesException as e:
                print(e)

    def calcular_salario(self):
        self.salario = (self.horas_trabajadas * self.tarifa_hora) - self.deducciones

    def imprimir_salario(self):

        return print("El salario de {} es: {}".format(self.nombre ,self.salario))

mario = Worker()
mario.asignar_valores()
mario.calcular_salario()
mario.imprimir_salario()

