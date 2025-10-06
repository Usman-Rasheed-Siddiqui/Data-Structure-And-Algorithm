
array = [10, 51, 18, 2]
print(array)

def InsertionSort(array):

    n = len(array)

    for i in range(1, n):
        x = array[i]
        j = i - 1

        while j >= 0 and array[j] > x:
            array[j+1] = array[j]
            j -= 1

        array[j+1]=x
        print(f"{i} Iteration: ", array)

array1 = InsertionSort(array)
print(array)
