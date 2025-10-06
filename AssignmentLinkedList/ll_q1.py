
from SinglyLinkedList import ListNode

def del_x(H, x):
    res = H.search(x)

    if res[0] == True:
        if res[2] == H:
            H = H.next
            res = H.search(x)
    
        while res[0]:
            if res[1] is None:
                H = H.next
            else:
                res[1].delete()

            res = H.search(x)

    return H

head = ListNode(30)

head.insert(30)     
head.insert(40)
head.insert(10)

head.traverse()
head = del_x(head, 30)
head.traverse()