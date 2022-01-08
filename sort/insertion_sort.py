# INSERTION SORT ALGORITHM

def insertion_sort(array):
    # the loop starts from the second element till the end
    for j in range(1,len(array)):
        # at every iteration the j-th value is saved in the 'key' variable
        key = array[j]
        i = j-1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]        
            i=i-1
        array[i+1] = key