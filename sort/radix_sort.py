# RADIX SORT ALGORITHM

def counting_sort_radix(A, digit):
    array = A[:] # Create a copy of the list to sort

    C = [0 for i in range(10)]

    for element in array:
        C[element//10**(digit-1) % 10] += 1

    for i in range(1,10):
        C[i] = C[i] + C[i-1]
    
    for j in range(len(array)-1, -1, -1):
        A[C[array[j] // 10 ** (digit-1) % 10] - 1] = array[j]
        C[array[j] // 10 ** (digit-1) % 10] -= 1

def radix_sort(array, num_digits):
    for digit in range(1, num_digits + 1):
        counting_sort_radix(array, digit)