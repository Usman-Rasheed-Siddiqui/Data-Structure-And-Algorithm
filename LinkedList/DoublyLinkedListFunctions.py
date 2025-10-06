
from DoublyLinkedList import DLNode

def buildlistright(value):
    node = DLNode(value[0])
    for i in range(1, len(value)):
        node.insertright(value[i])
        node = node.right
    
    return node

def buildlistleft(value):
    node = DLNode(value[0])
    for i in range(1, len(value)):
        node.insertleft(value[i])
        node = node.left
    
    return node


print("=== TEST 1: Build list using insertright ===")
head = buildlistright([10, 20, 30, 40])
head.traverse()  # should show 10 <-> 20 <-> 30 <-> 40 <-> None
print("Length:", len(head))  # should be 4


print("\n=== TEST 2: Build list using insertleft ===")
head2 = buildlistleft([10, 20, 30, 40])
head2.traverse()  # should show 40 <-> 30 <-> 20 <-> 10 <-> None
print("Length:", len(head2))  # should be 4


print("\n=== TEST 3: Insert at left and right of middle node ===")
mid = head.search(20)
mid.insertright(25)
mid.insertleft(15)
head.traverse()  # expected: 10 <-> 15 <-> 20 <-> 25 <-> 30 <-> 40 <-> None
print("Length after inserts:", len(head))


print("\n=== TEST 4: Delete a node ===")
target = head.search(25)
head, deleted = target.delete()
print(f"Deleted node: {deleted.data}")
head.traverse()  # expected: 10 <-> 15 <-> 20 <-> 30 <-> 40 <-> None
print("Length after delete:", len(head))


print("\n=== TEST 5: Delete head node ===")
target = head.search(10)
head, deleted = target.delete()
print(f"Deleted node: {deleted.data}")
head.traverse()  # expected: 15 <-> 20 <-> 30 <-> 40 <-> None


print("\n=== TEST 6: Search existing and non-existing values ===")
node = head.search(30)
print("Found:", node.data if node else "Not found")  # expected 30
node = head.search(100)
print("Found:", node.data if node else "Not found")  # expected Not found
