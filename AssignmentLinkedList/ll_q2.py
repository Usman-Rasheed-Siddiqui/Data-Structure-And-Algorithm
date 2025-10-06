
from SinglyLinkedList import ListNode


def count_x(H, x):
    
    count = 0
    a = H

    while a is not None:
        if a.data == x:
            count += 1
        a = a.next

    return count

head = ListNode(30)

head.insert(30)     
head.insert(40)
head.insert(10)

head.traverse()
count = count_x(head, 30)
print(count)


        

    

