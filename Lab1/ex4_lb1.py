
lst = [1, 2, 3, 4, (1, 2)]

print(f"Address of List: {id(lst)}")

count = 0
for element in lst:
    if not type(element) == tuple:
        count += 1
    else:
        print(f"Tuple found after {count} element/s")
        print(f"Address of tuple: {id(element)}")
        break
