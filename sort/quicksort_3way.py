# QUICKSORT 3-WAY ALGORITHM

def partition_3way(array, p, r):
    x = array[p]
    a = j = p
    b = r
    while j <= b:
        if array[j] < x:
            array[a], array[j] = array[j], array[a]
            a = a+1
            j = j+1
        elif array[j] > x:
            array[b], array[j] = array[j], array[b]
            b = b-1
        else:
            j = j+1

    index=[]
    index.append(a)
    index.append(b)
    return index

def quicksort_3way(array, first, last):
    if first < last:
        index = partition_3way(array, first, last)
        quicksort_3way(array, first, index[0]-1)
        quicksort_3way(array, index[1]+1, last)