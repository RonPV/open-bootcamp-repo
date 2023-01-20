from operaciones import *

def main():
	numero1 = 15
	numero2 = 5
	
	s = suma.sumar(numero1, numero2)
	r = resta.restar(numero1, numero2)
	m = multiplicacion.multiplicar(numero1, numero2)
	d = division.dividir(numero1, numero2)

	print(s)
	print(r)
	print(m)
	print(d)

if __name__ == "__main__":
	main()