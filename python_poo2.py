import math

class Student(object):
    def __init__(self):
        self.nombre = ''; self.cedula = ''; self.edad = ''

    def read_data(self):
        self.nombre = input("Insert your name here: ")
        self.cedula = input("Insert your number ID here: ")
        self.edad = input("Insert your age here: ")

    def print_name(self):
        if self.nombre != '':
            print("Your name is: {}".format(self.nombre))
        else:
            print("Not have name")

    def print_message(self):
        print("UNIVERSIDAD TENOLÓGICA")

    def average(self):
        try:
            self.note_one = float(input("Insert your first note here: "))
            self.note_two = float(input("Insert your second note here: "))

            average = ((self.note_one + self.note_two) / len([self.note_one, self.note_two]))

            return print("Your average is: {}".format(round(average,2)))

        except:
            return print("Notes have null value")


class EcuationOne(object):
    def __init__(self):
        self.a = 0.0; self.b = 0.0; self.c = 0.0; self.d = 0.0

    def read_values(self):
        self.a = float(input("Insert the value of A: "))
        self.b = float(input("Insert the value of B: "))
        self.c = float(input("Insert the value of C: "))
        self.d = float(input("Insert the value of D: "))

    def result(self):

        response = (self.a + self.b)/self.c * self.d
    
        return print(round(response, 2))
    

class Elevate(object):
    def __init__(self):
        self.number = 4; self.square = 0; self.cube = 0

    def elevate_numer(self):

        self.square = self.number ** 2
        self.cube = self.number ** 3

    def return_result(self):
        
        return print("The elevation of {} squared is: {} and cube is {}".format(self.number, self.square, self.cube))

# number = Elevate()
# number.elevate_numer()
# number.return_result()

class EcuationTwo(object):
    def __init__(self):
        self.a = 0; self.b = 0; self.c = 0; self.response = 0
        self.s = 0

    def asingment_values(self):
        self.a = float(input("Inser the value of A: "))
        self.b = float(input("Inser the value of B: "))
        self.c = float(input("Inser the value of C: "))

        self.s = ((self.a + self.b + self.c) / 2)

    def print_result(self):

        self.response = math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))

        return print(self.response)

ecuation = EcuationTwo()
ecuation.asingment_values()
ecuation.print_result()

def ecuation_instance():
    ecuation = EcuationOne()
    ecuation.read_values()
    ecuation.result()

#ecuation_instance()

def object_instance():

    diego = Student()
    diego.read_data()
    diego.print_name()
    diego.print_message()
    diego.average()

#object_instance()