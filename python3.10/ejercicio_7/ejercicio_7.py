class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):

        if(self.nota >= 6):
            print("El alumno", self.nombre, "aprobo con una nota de", self.nota)

        elif(self.nota < 6):
            print("El alumno", self.nombre, "reprobo con una nota de", self.nota)
        
        else:
            print("Error")

nombre = input("Ingrese el nombre del alumno:\n")
nota = int(input("Ingrese la nota del alumno:\n"))

a1 = Alumno(nombre, nota)
a1.resultado()