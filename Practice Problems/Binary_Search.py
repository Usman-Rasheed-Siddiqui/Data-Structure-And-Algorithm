
array = [2, 10, 18, 51]

def BinarySearch(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high)//2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

print(BinarySearch(array, 18))


def binary_search(data, item):
    beg = 0
    end = len(data) - 1
    mid = int((beg + end) / 2)

    while beg <= end and data[mid] != item:

        if item < data[mid]:
            end = mid - 1
        else:
            beg = mid + 1

        mid = int((beg + end) / 2)
    
    loc = mid
    if loc:
        return f"Item found at location '{loc}'"
    else:
        return "Item not found"

print(binary_search(array, 18))
