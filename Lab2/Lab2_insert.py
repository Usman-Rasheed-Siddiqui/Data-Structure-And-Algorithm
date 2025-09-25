import timeit

lst = [1, 2, 3]
print("\nInitial List:", lst)

def ins(lst, data, pos):

    list1 = lst[:pos]
    list2 = lst[pos:]
    list1.append(data)
    return list1 + list2

def func1():
    lst = [1, 2, 3]
    ins(lst, 6, 2)

def func2():
    lst = [1, 2, 3]
    lst.insert(6, 2)

print(f"Insertion using my function: {ins(lst, 6, 2)}")
lst.insert(2, 6)
print("Insertion using Python's function: ", lst)

execution_ins = timeit.timeit(func1, number=10000)
print(f"\nExecution time for ins() function : {execution_ins} seconds")
execution_py = timeit.timeit(func2, number=10000)
print(f"Execution time insert() function : {execution_py} seconds")

difference = execution_ins - execution_py
print(f'Difference (User - Python): {difference} seconds')


