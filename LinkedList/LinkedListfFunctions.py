
from SinglyLinkedList import ListNode

def insafter(head, x, value):
    res = head.search(x)
    if res[0] == True:
        res[2].insert(value)

def insbefore(head, x, value):
    res = head.search(x)
    if res[0] == True:
        if res[2] == head:
            new = ListNode(value)
            new.next = head
            head = new
        else:
            res[1].insert(value)

    return head

def delnode(head, x):
    res = head.search(x)
    if res[0] == True:
        if res[2] == head:
            tmp = head
            head = head.next

        else:
            tmp = res[1].delete()
    
    return [head, tmp]

def buildlist(value):
    assert len(value) > 0
    a = ListNode(value[0])
    b = a
    for i in range(1, len(value)):
        a.insert(value[i])
        a = a.next

    return b

def instail(head, x):
    if head is None:
        a = ListNode(x)
        return a
    a = head
    while a.next is not None:
        a = a.next

    a.insert(x)
    return head



# -------- TEST CASES --------

head = buildlist([10, 20, 30, 40])
print("Initial list:")
head.traverse()

insafter(head, 20, 25)
print("\nAfter inserting 25 after 20:")
head.traverse()

head = insbefore(head, 10, 5)
print("\nAfter inserting 5 before 10:")
head.traverse()

head = insbefore(head, 30, 28)
print("\nAfter inserting 28 before 30:")
head.traverse()

head, deleted = delnode(head, 5)
print("\nAfter deleting 5:")
head.traverse()
print("\nDeleted:", deleted.data if isinstance(deleted, ListNode) else deleted)

head, deleted = delnode(head, 25)
print("\nAfter deleting 25:")
head.traverse()
print("\nDeleted:", deleted.data if isinstance(deleted, ListNode) else deleted)

head = instail(head, 50)
print("\nAfter inserting 50 at tail:")
head.traverse()
print()


