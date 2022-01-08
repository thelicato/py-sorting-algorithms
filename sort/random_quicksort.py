# RANDOMIZED QUICKSORT ALGORITHM

from quicksort import partition
from random import *

def randomized_partition(array, p, r):
    i = randint(p, r)
    array[r], array[i] = array[i], array[r]
    return partition(array, p, r)

def randomized_quicksort(array, first, last):
    if first < last:
        q = randomized_partition(array, first, last)
        randomized_quicksort(array, first, q-1)
        randomized_quicksort(array, q+1, last)