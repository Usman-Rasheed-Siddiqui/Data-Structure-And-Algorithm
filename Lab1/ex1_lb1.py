
# print in triangle
x = int(input("enter the number: "))
for n in range(0, x):
    print(f"Value of n: {n} ID n: {id(n)} (Before)\nprinting: ", end= " ")
    n += 1
    print("*" * (0+n))
    print(f"Value of n: {n} ID n: {id(n)} (After)\n")

for n in range(-x, 0):
    print(f"Value of n: {n} ID n: {id(n)} (Before)\nprinting: ", end= " ")
    n += 1
    print("*" * (0 -n+1))
    print(f"Value of n: {n} ID n: {id(n)} (After)\n")

