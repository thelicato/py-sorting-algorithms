# HEAPSORT ALGORITHM

def max_heapify(array, n, i):
    l = (2*i)+1 # Left(i)
    r = (2*i)+2 # Right(i)
    largest=i
    if l < n and array[l] > array[largest]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

def build_max_heap(array):
    n = len(array)
    for i in range((len(array)//2)-1, -1, -1):
        max_heapify(array, n, i)

def heapsort(array):
    build_max_heap(array)
    n = len(array)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, i, 0)