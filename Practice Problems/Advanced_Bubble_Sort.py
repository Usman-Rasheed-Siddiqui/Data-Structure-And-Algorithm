

array = [10, 51, 18, 2]
print(array)

def BubbleSort(array):

    n = len(array)

    for i in range(n-1):
        found = False
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                found = True
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            else:
                found = False
        
        print(f"{i+1} Iteration: ", array)
        
        if not found:
            break
        
    return array


array1 = BubbleSort(array)
print(array)
