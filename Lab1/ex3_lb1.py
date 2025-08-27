
lst = [1, 2, 3, 3, 4, 5, 5, 6]
print(id(lst))

print(f"BEFORE {lst}\n")
for num in lst:
    print(f"ID of {num}: {id(num)}")

lst = set(lst)

lst = list(lst)


print(f"\nAFTER {lst}\n")

for num in lst:
    print(f"ID of {num}: {id(num)}")


print(id(lst))