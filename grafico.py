import tiempos
import matplotlib.pyplot as plt
import numpy as np
import sys
from subprocess import run
import glob
import os

# sys.argv[1] = Cantidad de experimentos a realizar
# sys.argv[2] = Cantidad máxima de elementos por lista
# sys.argv[3] = Intervalo de muestreo
if __name__ == '__main__':

	for i in range(0, int(sys.argv[1])):
		with open('datos_sorting'+str(i)+'.csv', 'w') as salida: 
			for j in tiempos.generar_lista_tuplas(int(sys.argv[2]), int(sys.argv[3])):
				salida.write(','.join(j) + '\n')

	# Genero una lista donde cada elemento es una matriz con la información de cada uno
	# de los experimentos realizados. Luego, calculo el tiempo promedio de cada algoritmo
	# para cada una de las longitudes de las listas evaluadas
	aux = [np.loadtxt('datos_sorting'+str(i)+'.csv', delimiter=',') for i in range(0, int(sys.argv[1]))]
	datos = sum(aux)/len(aux)

	# Grafico todo
	plt.plot(datos[:,0], datos[:,1], label='selectionSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,2], label='insertionSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,3], label='bubbleSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,4], label='mergeSort', linewidth=2)
	plt.plot(datos[:,0], datos[:,5], label='quickSort', linewidth=2)
	plt.xlabel('Cantidad de elementos', color='black')
	plt.ylabel('Tiempo de ejecucion (s)', color= 'black')
	plt.legend(loc=2)
	plt.show()

	# Borro los archivos .csv que se generaron en cada experimentos
	for fl in glob.glob("datos_sorting*.csv"):
	    #Do what you want with the file
	    os.remove(fl)