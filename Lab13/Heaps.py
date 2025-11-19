

def HeapInsert(array, x):
    if not array:
        array.append(x)
        return array

    array.append(x)
    i = len(array) - 1

    while i > 0:
        parent = (i - 1)//2
        if array[parent] <= array[i]:
            break
        else:
            array[parent], array[i] = array[i], array[parent]
            i = parent

    return array

def HeapDelete(array):
    if not array:
        return array

    min = array[0]
    last = array.pop()
    if array:
        array[0] = last

        i = 0
        size = len(array)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < size and array[left] < array[smallest]:
                smallest = left
            if right < size and array[right] < array[smallest]:
                smallest = right

            if smallest == i:
                break

            array[i], array[smallest] = array[smallest], array[i]
            i = smallest

    return array, min

array = [1, 5, 3, 12, 8, 9, 7]
print("Heap:", array)

array = HeapInsert(array, 4)
print("Inserting: 4")
print("Heap after Insertion:", array)

array, min = HeapDelete(array)
print("Deleted Minimum Value:", min)
print("Heap after Deletion:", array)
