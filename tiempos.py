import sorting
import random
import time
import copy

def generar_tupla(n):
	lista_insertion = [random.random() for i in range(0, n)]
	lista_selection = copy.deepcopy(lista_insertion)
	lista_bubble = copy.deepcopy(lista_insertion)
	lista_merge = copy.deepcopy(lista_insertion)
	lista_quck = copy.deepcopy(lista_insertion)
	tiempo_1 = time.clock()
	sorting.insertionSort(lista_insertion)
	tiempo_2 = time.clock()
	sorting.selectionSort(lista_selection)
	tiempo_3 = time.clock()
	sorting.bubbleSort(lista_bubble)
	tiempo_4 = time.clock()
	sorting.mergeSort(lista_merge)
	tiempo_5 = time.clock()
	sorting.quickSort(lista_quck)
	tiempo_6 = time.clock()
	return str(n), str(tiempo_2-tiempo_1), str(tiempo_3-tiempo_2), str(tiempo_4-tiempo_3), str(tiempo_5-tiempo_4), str(tiempo_6-tiempo_5)

		
def generar_lista_tuplas(n, k):
	ls = []
	i = 0
	for i in range(10, n+1, k):
		ls.append(generar_tupla(i))
		i += 1
	return ls
