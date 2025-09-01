
# print triangle and address of n

x = int(input("enter the number: "))    # Input

# First loop
for n in range(0, x):
    print(f"Value of n: {n} ID n: {id(n)} (Before)\nprinting: ", end= " ")  # Print ID's before
    n += 1
    print("*" * (0+n))
    print(f"Value of n: {n} ID n: {id(n)} (After)\n")   # Print ID's after

# Second loop
for n in range(-x, 0):
    print(f"Value of n: {n} ID n: {id(n)} (Before)\nprinting: ", end= " ")      # Print ID's before
    n += 1
    print("*" * (0 -n+1))
    print(f"Value of n: {n} ID n: {id(n)} (After)\n")   # Print ID's after


