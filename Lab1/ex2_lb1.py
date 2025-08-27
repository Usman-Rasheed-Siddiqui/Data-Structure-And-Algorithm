
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print(f"Address of {dic1}: {id(dic1)}")
print(f"Address of {dic2}: {id(dic2)}")
print(f"Address of {dic3}: {id(dic3)}")


new_dic = {}
new_dic.update(dic1)        # Pipe operator to concatenate dictionaries
new_dic.update(dic2)
new_dic.update(dic3)

print(f"\nNew Dic: {new_dic}")
print(f"Address of new dict: {id(new_dic)}\n")


for key, value in new_dic.items():
    print(f"ID of ({key}: {value}): ({id(key)}: {id(value)})")