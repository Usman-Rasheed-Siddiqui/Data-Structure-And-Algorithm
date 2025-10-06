from DoublyLinkedList import DLNode

def MaxDlist(H):
    
    max_num = H.data
    a = H
    while a is not None:
        if a.data > max_num:
            max_num = a.data
        a = a.right
    
    b = H.left
    while b is not None:
        if b.data > max_num:
            max_num = b.data
        b = b.left
        
    return max_num

ll = DLNode(10)
ll.insertleft(20)
ll.insertleft(30)
ll.insertright(40)
ll.insertright(50)
ll.traverse()
max_number = MaxDlist(ll)
print(max_number)

