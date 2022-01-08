# QUICKSORT ALGORITHM

def partition(array, p, r):
    x = array[r]
    i = p-1
    for j in range(p,r):
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def quicksort(array, first, last):
    if first < last:
        q = partition(array, first, last)
        quicksort(array, first, q-1)
        quicksort(array, q+1, last)