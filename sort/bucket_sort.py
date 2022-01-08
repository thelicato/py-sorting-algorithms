# BUCKET SORT ALGORITHM

from insertion_sort import *

def bucket_sort(array):
    n = len(array)
    
    B = [[]for i in range(n)]
    for i in range(n):
        # Insert A[i] into list B[[nA[i]]
        index = int(n*array[i])
        B[index].append(array[i])
    
    for i in range(n):
        # Sort list B[i] with insertion sort
        insertion_sort(B[i])

    # Concatenate the lists B[0],....,B[n-1] in order
    C = []
    for i in range(n):
        C = C + B[i]
    return C