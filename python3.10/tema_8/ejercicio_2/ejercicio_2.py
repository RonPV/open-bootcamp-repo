import pickle

class Vehiculo:

    def __init__(self, puertas, ruedas):
        self.puertas = puertas
        self.ruedas = ruedas

    def añadirPuertas(self):
        self.puertas +=1
    
    def quitarPuertas(self):
        self.puertas -=1
    
    def añadirRuedas(self):
        self.ruedas +=1

    def quitarRuedas(self):
        self.ruedas -=1

    def __str__(self):
        return f'El número de puertas es {self.puertas} y el número de ruedas es {self.ruedas}.'

coche = Vehiculo(2,4)


archivo = open('save.bin', 'wb')
pickle.dump(coche, archivo)
archivo.close()

coche.añadirPuertas()
coche.añadirRuedas()

print(coche)

archivo = open('save.bin', 'rb')
coche = pickle.load(archivo)

print(coche)