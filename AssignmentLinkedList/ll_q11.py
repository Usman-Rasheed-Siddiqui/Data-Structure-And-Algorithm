
from SinglyLinkedList import ListNode

def bubblesort(H):
    
    if H is None:
        return
    if H.next is None:
        return
    a = H
    done = None
    while a.next != done:
        b = a
        while b.next != done:
            if b.data > b.next.data:
                b.data, b.next.data = b.next.data, b.data

            if b.next.next == done:
                done = b.next
                break

            else:
                b = b.next
    return

ll = ListNode(10)
ll.insert(90)
ll.insert(100)
ll.insert(37)
ll.insert(45)
ll.traverse()
bubblesort(ll)
ll.traverse()


