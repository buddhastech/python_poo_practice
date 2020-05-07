class Person(object):
    
    def __init__(self):
        self.cedula = '702665471'

    def show_data(self, **kwargs):

        print("Cedula: ", self.cedula)
        for key, value in kwargs.items(): # Loop for kwargs items
            print(key,": ", value)

class Estudent(Person):

    def __init__(self):
        Person.__init__(self)
        Person.show_data(self, nombre = "Diego", edad = 21, correo = "dgduarte14@hotmail.com")
        
Diego = Estudent()
