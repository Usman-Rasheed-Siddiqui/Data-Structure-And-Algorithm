
from Lab7_exa import Stack

s = Stack(10)
s.display()
print("isEmpty Operation:")
check = s.isEmpty()
print("Yes" if check else "No")
print("\nPush Operation:")
s.push(1)
s.push(2)
s.push(3)
s.display()
print("isEmpty Operation:")
check = s.isEmpty()
print("Yes" if check else "No")
print("\nPop Operation:")
item = s.pop()
print("Item Popped:", item)
s.display()
print("Top Operation:")
top = s.top()
print("Top Item:", top)

