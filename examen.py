from exceptions.exceptions import ValidationsMethods as validation

class Persona(object): # Clase Persona
    
    def __init__(self): # Constructor que contiene los atributos de persona
        self.nombre = ''
        self.apellidos = ''
        self.cedula = ''
        self.grupo = ''
        self.lugar_residencia = ''
        self.edad = ''


    def asignar_valores(self):  # método para asignar los valores a los atributos
        while True:
            self.cedula = input("Ingrese la cedula del estudiante: ")
            if validation.validar_cedula(self, self.cedula):  # método para validación de la cedula

                self.nombre = input("Ingrese el nombre del estudiante: ")
                if validation.validar_nombre(self, self.nombre):

                    self.apellidos = input("Ingrese los apellidos del estudiante: ")
                    if validation.validar_apellidos(self, self.apellidos):

                        self.edad = input("Ingrese la edad del estudiante: ")
                        if validation.validar_edad(self, self.edad):

                            self.grupo = input("Ingrese el grupo al que pertenec [ A, B, C ]: ")
                            if self.grupo == 'A' or self.grupo == 'B' or self.grupo == 'C':
                                self.lugar_residencia = input("Ingrese el nombre del barrio donde vive: ")
                                break
                            else:
                                print("Ingrese un grupo valido")
                        else:
                            print("Ingrese una edad valida")
                    else:
                        print("Ingrese apellidos validos")
                        
                else:
                    print("Ingrese un nombre valido")

            else:
                print("Ingrese una cedula valida")
    
class Puntaje(Persona):  # Clase Puntaje
    def __init__(self):  # método constructor de la clase Puntaje
        Persona.__init__(self)  # llamada del método constructor de la clase Persona
        self.respuestas_examen = []  # arreglo para almacenar las respuestas del examen
        self.respuestas_estudiante = []  # arreglo para almacenar las respuestas del estudiante
        self.respuestas_correctas = 0
        self.respuestas_incorrectas = 0

    def leerRespuestasEstudiante(self):
        archivo = input("Ingrese el nombre del examen del estudiante con la extensión .txt: ")
        try:
            with open('examenes_estudiantes/' + str(archivo), 'r') as examen_estudiante:
            
                respuestas = examen_estudiante.read()
                for respuesta in respuestas:
                    if respuesta != '\n':
                        self.respuestas_estudiante.append(respuesta)

        except FileNotFoundError as error:
            print("File Not Found: ", error)

    def leerRespuestasExamen(self):
        archivo  = input("Ingrese el nombre del examen con la extensión .txt: ")

        try:
            with open('examenes/' + str(archivo), 'r') as examen:
                respuestas = examen.read()
                for respuesta in respuestas:
                    if respuesta != '\n':
                        self.respuestas_examen.append(respuesta)

        except FileNotFoundError as error:
            print("File Not Found: ", error)

    def validar_respuestas(self):
        # compara las respuestas de abajo hacía arriba
        # entre las respuestas del examen y las respuestas del estudiante
        contador = -1
        for respuesta in self.respuestas_examen:
            contador += 1
            if self.respuestas_estudiante[contador] == self.respuestas_examen[contador]:
                self.respuestas_correctas += 1
            else:
                self.respuestas_incorrectas += 1

    def mostrar_datos(self):

        print("\nCedula: {}\nNombre: {}\nApellidos: {}\nGrupo: {}\nLugar: {}\nEdad{}".format(self.cedula,
        self.nombre, self.apellidos, self.grupo, self.lugar_residencia, self.edad))
        
        print("Respuestas correctas: {}\nRespuestas Incorrectas: {}".format(self.respuestas_correctas,
        self.respuestas_incorrectas))

        if self.respuestas_correctas >= 15:
            print('\n * Aprobado * \n')
        else:
            print('\n * Reprobado * \n')

    def menu(self):
        while True:
            menu_respuesta = input("""1- Leer datos de estudiante
            \n2- Leer examen
            \n3-Leer respuestas estudiante
            \n4-Validar respuestas
            \n5-Mostrar datos
            \n6-Salir
            \n Inserte la opción que desea: """)
            if menu_respuesta == '1':
                self.asignar_valores()
            
            elif menu_respuesta == '2':
                self.leerRespuestasExamen()
            
            elif menu_respuesta == '3':
                self.leerRespuestasEstudiante()
            
            elif menu_respuesta == '4':
                self.validar_respuestas()
            
            elif menu_respuesta == '5':
                self.mostrar_datos()
            
            elif menu_respuesta == '6':
                break

Diego = Puntaje()  # objeto Puntaje
Diego.menu()
