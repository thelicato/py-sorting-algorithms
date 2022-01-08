# MERGE SORT ALGORITHM

import sys

def merge(array, lefthalf, righthalf):
    lefthalf.append(sys.maxsize)
    righthalf.append(sys.maxsize)
    j = 0
    i = 0
    for k in range(len(array)):
        if lefthalf[i] <= righthalf[j]:
            array[k] = lefthalf[i]
            i = i+1
        else:
            array[k] = righthalf[j]
            j = j+1

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2  # Integer divison (rounded down)
        lefthalf = array[:mid] # Takes the first half of the list
        righthalf = array[mid:] # Takes the second half of the list
        # Recursive calls for both sub-arrays
        merge_sort(lefthalf)
        merge_sort(righthalf)     
        merge(array, lefthalf, righthalf)