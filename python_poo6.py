class MinimumValueException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def __str__(self):
        return 'MinumumValueException: {}'.format(self.mensaje)


numero = 100
try:
    if numero < 150:
        raise MinimumValueException('El número {} es menor a 100'.format(numero))

    # raise llama a la clase pero además la imprime, con lo que
    # al tener el método __str__ se imprime lo que hay ahí porque imprime la instancia
    
    else:
        print("Número mayor a 100")

except MinimumValueException as e:
    print(e)