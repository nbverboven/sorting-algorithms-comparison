import tiempos
import matplotlib.pyplot as plt
import numpy as np
import sys

# sys.argv[1] = Cantidad de experimentos a realizar
# sys.argv[2] = Cantidad máxima de elementos por lista
# sys.argv[3] = Intervalo de muestreo
if __name__ == '__main__':

	# Genero una lista donde cada elemento es una matriz con la información de cada uno
	# de los experimentos realizados. Luego, calculo el tiempo promedio de cada algoritmo
	# para cada una de las longitudes de las listas evaluadas
	aux = []
	for i in range(0, int(sys.argv[1])):
		aux.append( tiempos.generar_matriz_tiempos(int(sys.argv[2]), int(sys.argv[3])) )
	datos = sum(aux)/len(aux)

	# Grafico todo
	plt.plot(datos[:,0], datos[:,1], label='insertionSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,2], label='selectionSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,3], label='bubbleSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,4], label='mergeSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,5], label='quickSort', linewidth=2)
	plt.xlabel('Cantidad de elementos', color='black')
	plt.ylabel('Tiempo de ejecucion (s)', color= 'black')
	plt.legend(loc=2)
	plt.show()