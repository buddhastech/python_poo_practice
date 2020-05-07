class Person(object):
    def __init__(self):
        self.nombre = "Diego"

    def __str__(self):
        return "Name: {}".format(self.nombre)


class Estudent(Person):
    def __init__(self):
        Person.__init__(self)

    def show_name(self):
        print("Your name is: ", self.nombre)


if __name__ == "__main__":

    Diego = Estudent()
    Diego.show_name()