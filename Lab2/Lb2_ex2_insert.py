
import timeit

# Dictionary
print("\nIntial Dictionary:",{1: "one", 3: "three"})

def ins_dic(dic, key, value):

    dic.update({key: value})
    return dic

def func1():
    dic = {1: "one", 3: "three"}
    ins_dic(dic, 2, "two")

def func2():
    dic = {1: "one", 3: "three"}
    dic[2] = "two"

temp_dic = {1: "one", 3: "three"}
print("Insertion using my function:", ins_dic(temp_dic, 2, "two"))

temp_dic[2] = "two"
print("Insertion using Python's function:", temp_dic)

execution_user = timeit.timeit(func1, number=10000)
print(f"\nMy time: {execution_user} sec")

execution_py = timeit.timeit(func2, number=10000)
print(f"Python's time: {execution_py} sec")

difference = execution_user - execution_py
print(f'\nDifference (User - Python): {difference} sec')


# Tuple
print("\nInitial Tuple:",(1, "two", {}, [4]))
def ins_tple(tple, data, pos):

    tple1 = tple[:pos]
    tple2 = tple[pos:]
    tple1 += (data, )

    return tple1 + tple2

def func3():
    tple = (1, "two", {}, [4])
    ins_tple(tple, 6, 2)

def func4():
    tple = (1, "two", {}, [4])
    tple = tple[:2] + (6, ) + tple[2:]

temp_tple = (1, "two", {}, [4])
print("Insertion using my function:", ins_tple(temp_tple, 6, 2))

temp_tple = (1, "two", {}, [4])
temp_tple = temp_tple[:2] + (6, ) + temp_tple[2:]
print("Insertion using Python's function:", temp_tple)


execution_user2 = timeit.timeit(func3, number=10000)
print(f"\nMy time: {execution_user2} sec")

execution_py2 = timeit.timeit(func4, number=10000)
print(f"Python's time: {execution_py2} sec")

difference = execution_user2 - execution_py2
print(f'\nDifference (User - Python): {difference} sec')
print()