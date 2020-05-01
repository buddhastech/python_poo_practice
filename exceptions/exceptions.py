class ZeroValuesException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):

        return "ZeroValueException: {}".format(self.mensaje)

class ValidationsMethods(object):

    def validar_cedula(self,cedula):
        digitos = ['0','1','2','3','4','5','6','7','8','9']

        response = False
        for digito in cedula:
            if digito in digitos:
                response = True   

            if not(digito in digitos):
                return False

        return response
    
    def validar_nombre(self,nombre):
        numeros_caracterest = ['0','1','2','3','4','5','6','7','8','9']

        response = False

        for caracter in nombre:
            if caracter in numeros_caracterest:
                return False
            else:
                response = True

        return response

    def validar_apellidos(self,apellidos):

        numeros_caracterest = ['0','1','2','3','4','5','6','7','8','9']

        response = False

        for caracter in apellidos:
            if caracter in numeros_caracterest:
                return False
            else:
                response = True

        return response

    def validar_edad(self,edad):
        numeros = ['0','1','2','3','4','5','6','7','8','9']

        response = False
        for numero in edad:
            if numero in numeros:
                response = True   

            if not(numero in numeros):
                return False

        return response

