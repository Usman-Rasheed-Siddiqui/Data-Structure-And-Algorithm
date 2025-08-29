

import timeit

lst = [1, 2, 3]

def ins(lst, data, pos):

    list1 = lst[:pos]
    list2 = lst[pos:]

    list1.append(data)

    return list1 + list2


def func1():
    ins(lst, 6, 2)


execution_delete = timeit.timeit(func1, number=1)
print(f"Execution time for ins() function : {execution_delete} seconds")


def func2():
    lst.insert(6, 2)


execution_py = timeit.timeit(func2, number=1)
print(f"Execution time insert() function : {execution_py} seconds")