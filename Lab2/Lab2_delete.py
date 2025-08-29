import timeit

lst = [1, 2, 3]

def dele(lst, data):

    for i in range(len(lst)):
        if lst[i] == data:
            list1 = lst[:i]
            list2 = lst[i+1:]

            return list1 + list2

def func1():
    dele(lst, 2)



execution_dele = timeit.timeit(func1, number=1)
print(f"Execution time for dele() function: {execution_dele} seconds")


def func2():
    lst.remove(2)
    print(lst)


execution_py = timeit.timeit(func2, number=1)
print(f"Execution time remove() function: {execution_py} seconds")
