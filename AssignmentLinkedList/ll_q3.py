from SinglyLinkedList import ListNode

def del_tail(H):

    precursor = H
    cursor = H.next

    if H.next is None:
        a = H
        H = H.next
        return H, a
    
    while cursor.next is not None:
        precursor = cursor
        cursor = cursor.next

    precursor.next = cursor.next

    return head, cursor

head = ListNode(30)

head.insert(30)     
head.insert(40)
head.insert(10)

head.traverse()
head, delete = del_tail(head)
print(delete.data)
head.traverse()


    