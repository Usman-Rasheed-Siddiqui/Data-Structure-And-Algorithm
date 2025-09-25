
import timeit

# Dictionary
print("\nInitial Dictionary:",{1: "one", 2:"two", 3: "three"})

def del_dict(dic, data):

    new_dict = {}
    for key, value in dic.items():
        if key!= data:
            new_dict[key] = value
    
    return new_dict

def func1():
    dic = {1: "one", 2:"two", 3: "three"}
    del_dict(dic, 3)

def func2():
    dic = {1: "one", 2:"two", 3: "three"}
    del dic[3]

temp_dic = {1: "one", 2: "two", 3: "three"}
print("Deletion using my function:", del_dict(temp_dic, 3))

temp_dic = {1: "one", 2: "two", 3: "three"}
del temp_dic[3]
print("Deletion using Python's function:", temp_dic)

execution_user = timeit.timeit(func1, number=10000)
print(f"\nExecution time for my function: {execution_user} seconds")

execution_py = timeit.timeit(func2, number=10000)
print(f"Execution time for built-in function: {execution_py} seconds")

difference = execution_user - execution_py
print(f'\nDifference (User - Python): {difference} seconds')


# Tuple
print("\nInitial Tuple:",(1, [4], {3: "Three"}, "two"))

def del_tple(tple, data):
    for i in range(len(tple)):
        if tple[i] == data:
            return tple[:i] + tple[i+1:] 
        
def func3():
    tple = (1, [4], {3: "Three"}, "two")
    del_tple(tple, "two")

def func4():
    tple = (1, [4], {3: "Three"}, "two")
    tple = (item for item in tple if item != "two")

temp_tple = (1, [4], {3: "Three"}, "two")
print("Deletion using my function:", 
      del_tple(temp_tple, "two"))

temp_tple = (1, [4], {3: "Three"}, "two")
print("Deletion using Python's function:", 
      tuple(item for item in temp_tple if item != "two"))

execution_user2 = timeit.timeit(func3, number=10000)
print(f"\nExecution time for my function: {execution_user2} seconds")

execution_py2 = timeit.timeit(func4, number=10000)
print(f"Execution time for built-in function: {execution_py2} seconds")

difference = execution_user2 - execution_py2
print(f'\nDifference (User - Python): {difference} seconds')


print()