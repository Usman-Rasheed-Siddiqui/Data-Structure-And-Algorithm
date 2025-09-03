# Binary operation is a logarithmic operation

import timeit

def binary_search(data, item, verbose):

    beg = 0
    end = len(data) - 1
    mid = int((beg + end) / 2)

    while beg <= end and data[mid] != item:
        if verbose:
            print("\nBeginning:", data[beg])
            print("Middle:", data[mid])
            print("End:", data[end])
        if item < data[mid]:
            end = mid - 1
        else:
            beg = mid + 1

        mid = int((beg + end) / 2)

    if data[mid] == item:
        if verbose:
            print("\nBeginning:", data[beg])
            print("Middle:", data[mid])
            print("End:", data[end])
        loc = mid
    else:
        loc = None

    return f"\nItem found at location '{loc}'" if loc is not None else "Item not found"


data = input('\nEnter a list with spaces: ').split()

if all(isinstance(item, int) for item in data):
    data = [int(item) for item in data]

elif all(isinstance(item, float) for item in data):
    data = [float(item) for item in data]

item = input("Enter the digit/alphabet you want to find: ")

binary_search(data, item, verbose=True)

def func1():
    return binary_search(data, item, verbose=False)

def func2():
    try:
        data.index(item)
    except ValueError:
        print("Item not found")

execution_search = timeit.timeit(func1, number=10000)

search = func1()
print(search)

print(f"\nMy time: {execution_search} sec")

execution_py = timeit.timeit(func2, number=10000)
print(f"Python's time: {execution_py} sec")

difference = execution_search - execution_py
print(f'Difference (User - Python): {difference} sec')