

def capitalizar_lista(lista):

	lista_nueva=[]
	for item in lista:
		lista_nueva.append(item.capitalize())
	return set(lista_nueva)

def main():
	
	lista = set(input('Ingrese los paises separados por comas: \n').split(','))
	lista = sorted((capitalizar_lista(lista)))
	print(lista)
	
if __name__ == "__main__":
	main()
