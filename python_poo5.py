class Triangle(object):

    def __init__(self):
        self.base = float()
        self.height = float()
        self.result = float()
        self.signal = True

    def insertar_valores(self):
        
        while self.signal:
            try:
                self.base = float(input("Inserte el valor de la base: "))
                self.height = float(input("Inserte el valor de la altura: "))

                if self.base == 0 or self.height == 0:
                    print("Ingrese valores mayor a 0")
                
                else:
                    self.signal = False

            except ValueError as exe:  # el as permite acceder al mensaje
                # que provoca dicha excepción y guardarlo como exe
                print(exe)  

    def calcular_area(self):
        self.result = (self.base * self.height) // 2

    def imprimir_resultado(self):
        
        return print("El área del triangulo es: {}".format(self.result))

objeto = Triangle()
objeto.insertar_valores()
objeto.calcular_area()
objeto.imprimir_resultado()
