
import timeit
# Search

# Dictionary:
print("\nInitial Dictionary:",{1: "one",2:"two", 3: "three"})

def search_dic(dic, data):
    for key, value in dic.items():
        if key == data:
            return value

def func1():
    dic = {1: "one",2:"two", 3: "three"}
    search_dic(dic, 3)

def func2():
    dic = {1: "one",2:"two", 3: "three"}
    value = dic.get(3)

temp_dic = {1: "one", 2: "two", 3: "three"}
print("Search using my function:", search_dic(temp_dic, 3))
print("Search using Python's function:", temp_dic.get(3))

execution_user = timeit.timeit(func1, number=10000)
print(f"\nExecution time for my function: {execution_user} seconds")

execution_py = timeit.timeit(func2, number=10000)
print(f"Execution time for built-in function: {execution_py} seconds")

difference = execution_user - execution_py
print(f'\nDifference (User - Python): {difference} seconds')

# Tuple
print("Initial Tuple:",(1, "two", {3: "Three"}, [4]))

def search_tuple(tple, data):
    for i in range(len(tple)):
        if tple[i] == data:
            return i
        
def func3():
    tple = (1, "two", {3: "Three"}, [4])
    search_tuple(tple, "two")

def func4():
    tple = (1, "two", {3: "Three"}, [4])
    tple.index("two")

temp_tple = (1, "two", {3: "Three"}, [4])
print("Search using my function:", search_tuple(temp_tple, "two"))
print("Search using Python's function:", temp_tple.index("two"))

execution_user2 = timeit.timeit(func3, number=10000)
print(f"\nExecution time for my function: {execution_user2} seconds")

execution_py2 = timeit.timeit(func4, number=10000)
print(f"Execution time for built-in function: {execution_py2} seconds")

difference = execution_user2 - execution_py2
print(f'\nDifference (User - Python): {difference} seconds')
print()