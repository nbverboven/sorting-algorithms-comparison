import tiempos
import matplotlib.pyplot as plt
import numpy as np
import sys

cant_experimentos = int(sys.argv[1])
cant_max_elem_lista = int(sys.argv[2])
intervalo_muestreo = int(sys.argv[3])

# Genero una lista donde cada elemento es una matriz con la información de cada uno
# de los experimentos realizados. Luego, calculo el tiempo promedio de cada algoritmo
# para cada una de las longitudes de las listas evaluadas
datos_experimentales = []
for i in range(0, cant_experimentos):
	datos_experimentales.append( tiempos.generar_matriz_tiempos(cant_max_elem_lista, intervalo_muestreo) )
resultados = sum(datos_experimentales)/len(datos_experimentales)

# Grafico todo
plt.plot(resultados[:,0], resultados[:,1], label='insertionSort', linewidth=2)
plt.plot(resultados[:,0], resultados[:,2], label='selectionSort', linewidth=2)
plt.plot(resultados[:,0], resultados[:,3], label='bubbleSort', linewidth=2)
plt.plot(resultados[:,0], resultados[:,4], label='mergeSort', linewidth=2)
plt.plot(resultados[:,0], resultados[:,5], label='quickSort', linewidth=2)
plt.xlabel('Cantidad de elementos', color='black')
plt.ylabel('Tiempo de ejecucion (s)', color= 'black')
plt.legend(loc=2)
plt.show()