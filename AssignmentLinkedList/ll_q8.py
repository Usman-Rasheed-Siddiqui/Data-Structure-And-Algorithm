from DoublyLinkedList import DLNode

def insInDlist(H, y, x):
    node = DLNode(x)
    res = H.search(y)
    a = res.right

    node.left = res
    node.right = a

    if a is not None:
        a.left = node
    
    if res is not None:
        res.right = node

    return H

ll = DLNode(10)
ll.insertleft(20)
ll.insertleft(30)
ll.insertright(40)
ll.insertright(50)
ll.traverse()
ll = insInDlist(ll, 40, 25)
ll.traverse()


