
import timeit

# Dictionary
dic = {1: "one", 3: "three"}

def ins(dic, key, value):

    dic1 = {key: value}
    dic.update(dic1)

    return dic

def func1():
    ins(dic, 2, "two")

execution_user = timeit.timeit(func1, number=1)
print(f"Execution time for my function: {execution_user} seconds")

def func2():
    dic[2] = "two"

execution_py = timeit.timeit(func2, number=1)
print(f"Execution time python function: {execution_py} seconds")


# Tuple

tple = (1, 2, 3, 4)

def ins(tple, data, pos):

    tple1 = tple[:pos]
    tple2 = tple[pos:]

    tple1.append(data)

    return tple1 + tple2


