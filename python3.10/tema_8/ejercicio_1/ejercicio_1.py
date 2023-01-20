def escribir_linea(fichero, dato):

	if not dato.endswith("\n"):
		dato += "\n"

	fichero_session = open(fichero, "a")
	fichero_session.writelines(dato)
	fichero_session.close()

def escribir_lista(fichero, datos):

	fichero_session = open(fichero, "a")

	for dato in datos:
		if not dato.endswith("\n"):
			dato += "\n"

		fichero_session.writelines(dato)
	
	fichero_session.close()

def main():
	mi_fichero = "fichero_1.txt"
	texto1 = "Hola."
	texto2 = ["He creado un fichero.", "Fin."]

	escribir_linea(mi_fichero, texto1)
	escribir_lista(mi_fichero, texto2)

if __name__ == "__main__":
	main()