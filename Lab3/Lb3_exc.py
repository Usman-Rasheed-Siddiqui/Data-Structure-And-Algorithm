# Binary operation is a logarithmic operation

def binary_search(data, item):

    beg = 0
    end = len(data) - 1
    mid = int((beg + end) / 2)

    for i in range(len(data)):
        while beg <= end and data[mid] != item:
            print("\nBeginning:", data[beg])
            print("Middle:", data[mid])
            print("End:", data[end])
            if item < data[mid]:
                end = mid - 1
            else:
                beg = mid + 1

            mid = int((beg + end) / 2)

    if data[mid] == item:
        loc = mid
        return f"Item found at location '{loc}'"
    else:
        data.append(item)
        sorted(data)
        return f"\nItem inserted at position {data.index(item)} as it was not found" \
               f"\nNew list: {data}"

order = input("Enter order [(ascending (a)/ descending (d)]: ").lower()
data = input('\nEnter a list with spaces: ').split()

if all(isinstance(item, int) for item in data):
    data = [int(item) for item in data]

elif all(isinstance(item, float) for item in data):
    data = [float(item) for item in data]

if order == 'a':
    if data != sorted(data):
        print("Data not sorted")
        exit()

if order == 'd':
    if data != sorted(data, reverse=True):
        print("Data not sorted")
        exit()

item = input("Enter the digit/alphabet you want to find: ")

search = binary_search(data, item)

print(search)