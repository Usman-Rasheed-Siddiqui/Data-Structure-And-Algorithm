import timeit

lst = [1, 2, 3]
print("\nInitial List:", lst)

def search(lst, data):

    for i in range(len(lst)):
        if lst[i] == data:
            return i

def func1():
    lst = [1, 2, 3]
    search(lst, 2)

def func2():
    lst = [1, 2, 3]
    lst.index(2)

print(f"My function: {search(lst, 2)}")
print("Python's function: ", lst.index(2))

execution_search = timeit.timeit(func1, number=10000)
print(f"\nMy time: {execution_search} sec")
execution_py = timeit.timeit(func2, number=10000)
print(f"Python's time: {execution_py} sec")

difference = execution_search - execution_py
print(f'Difference (User - Python): {difference} sec')
print()