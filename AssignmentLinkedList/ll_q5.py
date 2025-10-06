
from SinglyLinkedList import ListNode

def split(H):
    
    if H is None:
        return [None, None]

    cursor = H

    while cursor is not None:
        if cursor.data < 0:
            new = cursor.next
            cursor.next = None
            return [H, new]
        
        cursor = cursor.next

    [H, None]
        
head1 = ListNode(1)

head1.insert(7)     
head1.insert(6)
head1.insert(-5)


head1.insert(4)     
head1.insert(3)
head1.insert(2)

head1.traverse()

sub1, sub2 = split(head1)

sub1.traverse()
sub2.traverse()