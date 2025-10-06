from SinglyLinkedList import ListNode

def insB4tail(H, x):

    precursor = H
    cursor = H.next

    while cursor.next is not None:
        precursor = cursor
        cursor = cursor.next

    precursor.insert(x)

    return H

head = ListNode(10)

head.insert(40)
head.insert(20)
head.traverse()
head = insB4tail(head, 30)
head.traverse()