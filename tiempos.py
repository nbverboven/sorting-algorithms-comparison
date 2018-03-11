import sorting
import random
import time
import copy
import numpy as np

def generar_tiempos(n):
	lista_insertion = [random.random() for i in range(0, n)]
	lista_selection = copy.deepcopy(lista_insertion)
	lista_bubble = copy.deepcopy(lista_insertion)
	lista_merge = copy.deepcopy(lista_insertion)
	lista_quick = copy.deepcopy(lista_insertion)

	tiempo_1 = time.process_time()
	sorting.insertionSort(lista_insertion)
	tiempo_2 = time.process_time()
	sorting.selectionSort(lista_selection)
	tiempo_3 = time.process_time()
	sorting.bubbleSort(lista_bubble)
	tiempo_4 = time.process_time()
	sorting.mergeSort(lista_merge)
	tiempo_5 = time.process_time()
	sorting.quickSort(lista_quick)
	tiempo_6 = time.process_time()

	return np.asarray( (n, tiempo_2-tiempo_1, tiempo_3-tiempo_2, 
		                   tiempo_4-tiempo_3, tiempo_5-tiempo_4, 
		                   tiempo_6-tiempo_5) )


def generar_matriz_tiempos(n, k):
	ls = np.empty( (1, 6) )
	i = 0
	for i in range(10, n+1, k):
		if i == 10:
			ls = generar_tiempos(i) # Genero la primera fila de la matriz
		else:
			ls = np.vstack( (ls, generar_tiempos(i)) ) # Agrego la nueva fila abajo de la matriz
		i += 1
	return ls
