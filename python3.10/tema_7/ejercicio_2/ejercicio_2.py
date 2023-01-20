import time

def main():
	fecha_local = time.asctime(time.localtime()).split()
	hora_local = list(map(int,fecha_local[3].split(":")))

	if hora_local[0] >= 16:
		print("Ya es hora!")

	elif hora_local[0] < 16:
		tiempo_restante = 16 * 3600 - (hora_local[0] * 3600 + hora_local[1] * 60 + hora_local[2])
		horas_restante = int(tiempo_restante/3600)
		minutos_restante = int((tiempo_restante/60)%60)
		segundos_restamte = int(tiempo_restante%60%60)

		print("faltan",horas_restante,"",minutos_restante,"",segundos_restamte)


if __name__ == "__main__":
	main()