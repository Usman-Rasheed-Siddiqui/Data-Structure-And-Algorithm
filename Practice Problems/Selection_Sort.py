
array = [10, 51, 18, 2]
print(array)

def SelectionSort(array):
    n = len(array)

    for i in range(n-1):
        minpos = i
        for j in range(i+1, n):
            if array[minpos] > array[j]:
                minpos = j
        
        if minpos != i:
            array[minpos], array[i] = array[i], array[minpos]
        
        print(f"{i+1} Iteration: ", array)

    return array

array1 = SelectionSort(array)
print(array)


    