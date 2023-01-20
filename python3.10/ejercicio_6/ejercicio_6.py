class Vehiculo:
    color = "verde"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 4

coche = Coche()

print("El color del coche es ",coche.color)
print("El número de ruedas del coche es ",coche.ruedas)
print("El número de puertas del coche es ",coche.puertas)
print("La velocidad del coche es ",coche.velocidad)
print("La cilindrada del coche es ",coche.cilindrada)