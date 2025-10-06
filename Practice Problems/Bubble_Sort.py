

array = [10, 51, 18, 2]
print(array)

def BubbleSort(array):

    n = len(array)

    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        print(f"{i+1} Iteration: ", array)

    return array


array1 = BubbleSort(array)
print(array)
