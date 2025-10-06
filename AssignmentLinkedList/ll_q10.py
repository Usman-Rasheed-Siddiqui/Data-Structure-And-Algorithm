from SinglyLinkedList import ListNode

def insClist(H, y, x):
    res  = H.searchcircular(y)
    node = ListNode(x)

    if res is not None:
        node.next = res.next
        res.next = node

    return H

# # Create first node
head = ListNode(10)

# Test 1: Insert a few nodes
head.insert(20)     # List: 10 -> 20
head.insert(30)     # List: 10 -> 30 -> 20
head.insert(40)

head.traverse()
head.circularize()
head.traverseCircular()
head = insClist(head, 40, 25)
head.traverseCircular()