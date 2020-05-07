class Product(object):
    
    def __init__(self):
        self.name = input('Insert the product name: ')
        self.maker = input('Insert the maker name: ')
        self.weight = input('Insert the product weight: ')
        self.cost = input('Insert the cost: ')

    def show_data(self, *args):
        print("\nPRODUCT FACTURE\n")
        
        print("Name: {} \nMaker: {} \nWeight: {}\nCost: {}"
        .format(self.name, self.maker, self.weight, self.cost))
        
        if self.name == "Centrifugal Pump" or self.name == "centrifugal pump":

            print("Impeller Diameter: {} \nNumer Of Sheets: {} \nAxis Of Rotation: {}"
            .format(args[0], args[1], args[2]))

        elif self.name == "Diaphragm Pump" or self.name == "diaphragm pump":
            print("Diaphragm Material: {}".format(args[0]))
        
        elif self.name == "Piston Pump" or self.name == "piston pump":
            print("Piston Lenght: {} \nDiameter: {} \nNumber of Cylindres: {}"
            .format(args[0],args[1],args[2]))

        elif self.name == "Pressure Tank" or self.name == "pressure tank":
            print("Diameter: {} \nHeight: {}".format(args[0],args[1]))

        elif self.name == "Spherical Tank" or self.name == "spherical tank":
            print("Diameter: {} ".format(args[0]))

class CentrifugalPump(Product):

    def __init__(self):
        Product.__init__(self)
        self.impeller_diameter = input("Insert the impeller diameter: ")
        self.number_sheets = input("Insert the number of sheets: ")
        self.axis_rotation = input("Insert the axis rotation: ")

        Product.show_data(self, self.impeller_diameter,
        self.number_sheets, self.axis_rotation)


class DiaphragmPump(Product):

    def __init__(self):
        Product.__init__(self)
        self.diaphragm_material = input("Insert the diaphragm material")

        Product.show_data(self, self.diaphragm_material)

class PistonPump(Product):
    def __init__(self):
        Product.__init__(self)
        self.piston_length = input("Insert the Piston Length: ")
        self.diameter = input("Insert the Diameter: ")
        self.number_cylindres = input("Insert the number of cylindres: ")

        Product.show_data(self, self.piston_length, self.diameter, self.number_cylindres)

class PressureTank(Product):
    def __init__(self):
        Product.__init__(self)
        self.diameter = input("Insert the Diameter: ")
        self.height = input("Insert the height of the product: ")

        Product.show_data(self, self.diameter, self.height)

class SphericalTank(Product):
    def __init__(self):
        Product.__init__(self)
        self.diameter = input("Insert the Diameter: ")


        Product.show_data(self, self.diameter)

tank = PistonPump()