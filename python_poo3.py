class Numbers(object):
    def __init__(self):
        self.number_one = int()
        self.number_two = int()
        self.signal = True

    def read_values_numbers(self):
        while self.signal:

            try:
                self.number_one = int(input("Insert the value of number one: "))
                self.number_two = int(input("Insert the value of number two: "))

                if self.number_one == 0 or self.number_two == 0:
                    print("\nPlease insert a different value then 0")

                else:
                    self.signal = False

            except ValueError: 
                print("Insert int Values")

    def sum_numbers(self):

        return print("The sum between {} and {} is {}".format(self.number_one,
        self.number_two, self.number_one + self.number_two))

    def subtraction_numbers(self):

        return print("The subtraction between {} and {} is {}".format(self.number_one,
        self.number_two, self.number_one - self.number_two))

    def division_number(self):

        return print("The division between {} and {} is {}".format(self.number_one,
        self.number_two, self.number_one // self.number_two))

    def product_numbers(self):

        return print("The product between {} and {} is {}".format(self.number_one,
        self.number_two, self.number_one * self.number_two))
import sys

class Square(object):

    def __init__(self, l1, l2, l3, l4):
        try:
            self.l1 = int(l1)
            self.l2 = int(l2)
            self.l3 = int(l3)
            self.l4 = int(l4)
            
            self.resultado = 0
        except:
            print("Insert int values") 
            sys.exit()

    def calcular_area(self):

        self.resultado = self.l1 * self.l2 * self.l3 * self.l4

    def imprimir_area(self):

        return print("The area of the square is {}".format(self.resultado))

def object_square():
    square = Square(6,6,6,6)
    square.calcular_area()
    square.imprimir_area()

object_square()

def object_numbers():
    objeto = Numbers()
    objeto.read_values_numbers()
    objeto.sum_numbers()
    objeto.subtraction_numbers()
    objeto.division_number()
    objeto.product_numbers()

