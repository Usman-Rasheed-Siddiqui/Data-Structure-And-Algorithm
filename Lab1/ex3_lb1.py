
lst = [1, 2, 3, 3, 4, 5, 5, 6]
print("Initial List ID: ",id(lst))

print(f"\nBEFORE {lst}\n")
for num in lst:
    print(f"ID of {num}: {id(num)}")

lst = set(lst)

lst = list(lst)

print("\nFinal List ID: ",id(lst))

print(f"\nAFTER {lst}\n")

for num in lst:
    print(f"ID of {num}: {id(num)}")
