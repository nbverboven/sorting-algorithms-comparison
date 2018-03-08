from random import randint

#
# En este módulo se encuentran las implementaciones de los algoritmos de sorting
# utilizados.
#


##################################################################################
#                                Insertion sort 
##################################################################################
def insertionSort(array):
	i = 1
	while i < len(array):
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
		i += 1
	return array


##################################################################################
#                                Selection sort 
##################################################################################
def selectionSort(array):
	i = 0
	while i < len(array)-1:
		minimo = minPos(i, len(array)-1, array)
		array[minimo], array[i] = array[i], array[minimo]
		i += 1
	return array

# Requiere: 0 <= i <= j < |array|
def minPos(i, j, array):
	res = i
	count = i
	while count <= j:
		if array[count] < array[res]:
			res = count
		count += 1
	return res


##################################################################################
#                                Bubble sort 
##################################################################################
def bubbleSort(array):
	intercambiado = True
	n = len(array)-1
	while n > 0 and intercambiado:
		intercambiado = False
		for j in range(n):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				intercambiado = True
		n -= 1
	return array



##################################################################################
#                                Merge sort 
##################################################################################
def mergeSort(array):
	if len(array) <= 1:
		return array
	else:
		medio = len(array) // 2
		m1 = mergeSort(array[:medio])
		m2 = mergeSort(array[medio:])
		return combine(m1, m2)
	
def combine(l1, l2):
	res = []
	i = 0
	j = 0
	while i < len(l1) and j < len(l2):
		if l1[i] <= l2[j]:
			res.append(l1[i])
			i += 1
		else:
			res.append(l2[j])
			j += 1
	if i < len(l1):
		res += l1[i:]
	if j < len(l2):
		res += l2[j:]
	return res


##################################################################################
#                                Quick sort 
##################################################################################
def quickSort(array, begin=0, end=None):
	if end is None:
		end = len(array) - 1
	def _quickSort(array, begin, end):
		if begin >= end:
			return
		pivot = partition(array, begin, end)
		_quickSort(array, begin, pivot-1)
		_quickSort(array, pivot+1, end)
	# return _quickSort(array, begin, end)
	_quickSort(array, begin, end)
	return array

def partition(array, begin, end):
	pivot = randint(begin, end)
	array[pivot], array[end] = array[end], array[pivot]
	i = begin - 1
	for j in range(begin, end):
		if array[j] <= array[end]:
			i += 1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[end] = array[end], array[i+1]
	return i + 1
