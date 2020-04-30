from exceptions.exceptions import ZeroValuesException
from exceptions.exceptions import validar_cedula, validar_nombre, validar_apellidos

class Person(object):
    def __init__(self):
        self.id = ''
        self.name = ''
        self.surnames = ''

class WorkerSalary(Person):
    def __init__(self):
        self.tarifa_horas = 1500
        self.horas_trabajadas = 0
        self.salario_bruto = 0 
        self.deducciones = 0
        self.salario_neto = 0
        self.salario_bruto = 0
    
    def asingmen_data(self):

        while True:
            try:
                self.id = input("Ingrese su cedula: ")
                if validar_cedula(self.id):
                    self.name = input("Ingrese su nombre: ")

                    if validar_nombre(self.name):
                        self.surnames = input("Ingrese sus apellidos: ")

                        if validar_apellidos(self.surnames):
                            self.horas_trabajadas = int(input("Inserte la cantidad de horas que trabajó: "))

                            if self.horas_trabajadas == 0:
                                raise ZeroValuesException('Ingrese horas mayor a 0')
                            break

                        else:
                            print("Ingrese apellidos correctos")
                    else:
                        print("Ingrese un nombre correcto")
                else:
                    print("Debe introducir una cedula correcta")

            except ValueError:
                print("Ingrese una cantidad de horas válida")

            except ZeroValuesException as e:
                print(e)
            
    def calcular_salarios(self):
        self.salario_bruto = (self.horas_trabajadas * self.tarifa_horas)
        self.deducciones = self.salario_bruto * 10 // 100
        self.salario_neto = self.salario_bruto - self.deducciones

    def imprimir_datos(self):

        return print(""" Name: {}
        \n Surnames: {}
        \n Worked hours: {}
        \n Hourly rate: {}
        \nDeductions: {}
        \n Salary: {}
        \n Net Salary: {}
        \n """.format(self.name, 
        self.surnames, 
        self.horas_trabajadas,
        self.tarifa_horas,
        self.deducciones,
        self.salario_bruto,
        self.salario_neto))

Diego = WorkerSalary()
Diego.asingmen_data()
Diego.calcular_salarios()
Diego.imprimir_datos()