
from SinglyLinkedList import ListNode

def combine(L1, L2):

    a = L1
    b = L2
    while a.next is not None:
        a = a.next

    a.next = b

    return L1

head1 = ListNode(1)

head1.insert(2)     
head1.insert(3)
head1.insert(4)

head2 = ListNode(5)

head2.insert(6)     
head2.insert(7)
head2.insert(8)

head1.traverse()
head2.traverse()

new = combine(head1, head2)
new.traverse()
    

