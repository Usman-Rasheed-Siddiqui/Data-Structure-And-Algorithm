import timeit

lst = [1, 2, 3]
print("\nInitial List: ", lst)

def dele(lst, data):

    for i in range(len(lst)):
        if lst[i] == data:
            list1 = lst[:i]
            list2 = lst[i+1:]

            return list1 + list2

def func1():
    lst = [1, 2, 3]
    dele(lst, 2)
    

def func2():
    lst = [1, 2, 3]
    lst.remove(2)

print(f"Deletion using my function: {dele([1, 2, 3], 2)}")
lst.remove(2)
print("Deletion using Python's function: ", lst)

execution_dele = timeit.timeit(func1, number=10000)
print(f"\nExecution time for dele() function: {execution_dele} seconds")

execution_py = timeit.timeit(func2, number=10000)
print(f"Execution time remove() function: {execution_py} seconds")

difference = execution_dele - execution_py
print(f'Difference (User - Python): {difference} seconds')

