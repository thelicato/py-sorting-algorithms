# COUNTING SORT ALGORITHM

def counting_sort(A, k):
    B = [0 for i in range(len(A))] # Create a list of length len(A) and fill it with 0
    C = [0 for i in range(k+1)] # Create a list of length k+1 and fill it with 0
    
    for element in A:
        C[element] += 1
        # C[i] is the num of occurrences of i
    
    for i in range(1, k+1):
        C[i] += C[i-1]
        # C[i] is the num of occurrences of values <= i

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1

    return B