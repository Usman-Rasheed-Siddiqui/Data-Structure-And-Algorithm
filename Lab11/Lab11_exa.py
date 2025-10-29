
array = [10, 51, 18, 2, 3, 4, 6]
print("Before Sorting:", array)

def Insertion(array):

    n = len(array)

    for k in range(1, n):
        temp = array[k]
        ptr = k - 1

        while ptr >= 0 and array[ptr] > temp:
            array[ptr+1] = array[ptr]
            ptr -= 1

        array[ptr+1] = temp

array1 = Insertion(array)
print("After Sorting:", array)

