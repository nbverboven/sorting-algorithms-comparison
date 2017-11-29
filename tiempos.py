import sorting
import random
import time
import copy
import matplotlib.pyplot as plt
import numpy as np

def generar_puntos(n):
	l = [random.random() for i in range(0, n)]
	return l

def generar_tupla(n):
	l1 = generar_puntos(n)
	l2 = copy.deepcopy(l1)
	l3 = copy.deepcopy(l1)
	l4 = copy.deepcopy(l1)
	l5 = copy.deepcopy(l1)
	x = time.clock()
	sorting.insertionSort(l1)
	y = time.clock()
	sorting.selectionSort(l2)
	z = time.clock()
	sorting.bubbleSort(l3)
	u = time.clock()
	sorting.mergeSort(l4)
	g = time.clock()
	sorting.quickSort(l5)
	h = time.clock()
	return str(n), str(y-x), str(z-y), str(u-z), str(g-u), str(h-g)

def generar_lista_tuplas(n, k):
	ls = []
	i = 0
	for i in range(10, n+1, k):
		ls.append(generar_tupla(i))
		i += 1
	return ls