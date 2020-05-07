class Persona(object):
    
    def __init__(self):

        self.cedula = input("¿Cuál es su número de cedula?: ")
        self.nombre = input("¿Cuál es su nombre?: ")
        self.apellidos = input("¿Cuáles son sus apellidos?: ")
        self.puesto = input("¿Cuál es su puesto?: ")
    
    def __str__(self):
        
        return  "Objeto con nombre: {}".format(self.nombre)

class EmpleadoHora(Persona):
    
    def __init__(self):
        Persona.__init__(self)
        self.sueldo = 0
        self.horas_laboradas = int(input("Ingrese la cantidad de horas laboradas: "))
        self.tarifa_horas = 3500
        self.deducciones = 0
    
    def calcular_salario(self):

        self.sueldo = self.horas_laboradas * self.tarifa_horas
        self.deducciones = self.sueldo * 10 // 100
        self.sueldo = self.sueldo - self.deducciones

    def mostrar_datos(self):
        
        return print('''
        Boleta
=======================

Cedula: {}
Nombre: {}
Apellidos: {}
Puesto: {}
Cantidad de horas laboradas: {}
Tarifa por horas: {}
Deducciones: {}
Sueldo total: {}

======================='''.format(self.cedula, self.nombre,
        self.apellidos, self.puesto, self.horas_laboradas,
        self.tarifa_horas, self.deducciones, self.sueldo))

class EmpleadoPlanta(Persona):
    
    def __init__(self):
        Persona.__init__(self)
        self.extras = input("Ingrese el monto de extras a sumar: ")
        self.sueldo = int(input("Ingrese su salario base: ")) 
   
    def calcular_salario(self):
        
        try:
            self.extras = int(self.extras)
            self.sueldo += self.extras
            return 
    
        except:
            print("Usted no posee extras, su sueldo total es: {}".format(self.sueldo))    

    def mostrar_datos(self):
                return print('''
        Boleta
=======================

Cedula: {}
Nombre: {}
Apellidos: {}
Puesto: {}
Sueldo total: {}

======================='''.format(self.cedula, self.nombre,
        self.apellidos, self.puesto, self.sueldo))

Diego = EmpleadoPlanta()
Diego.calcular_salario()
Diego.mostrar_datos()