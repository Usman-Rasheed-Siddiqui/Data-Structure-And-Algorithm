import timeit

lst = [1, 2, 3]

def search(lst, data):

    for i in range(len(lst)):
        if lst[i] == data:
            return i

def func1():
    print(search(lst, 2))


execution_search = timeit.timeit(func1, number=1)
print(f"Execution time For search() function: {execution_search} seconds")


def func2():
    lst.index(2)


execution_py = timeit.timeit(func2, number=1)
print(f"Execution time for index() function : {execution_py} seconds")
