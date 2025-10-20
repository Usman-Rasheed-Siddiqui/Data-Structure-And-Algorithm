from SinglyLinkedList import ListNode

def newHead(H, x):
    res = H.search(x)

    if res[0]:
        H = res[2]
        return H
    
    return H

head = ListNode(10)

head.insert(50)
head.insert(40)
head.insert(30)
head.insert(20)
head.traverse()

head = newHead(head, 30)
head.traverse()
