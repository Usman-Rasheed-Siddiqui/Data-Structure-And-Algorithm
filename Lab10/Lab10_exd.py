
from LinkedList import LinkedList, Node

class QueueLL:
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.linkedlist = LinkedList()
        self.size = 0
        self.front = 0
        self.rear = self.maxlength - 1

    def makeNull(self):
        self.size = 0
        self.front = 0
        self.rear = self.maxlength - 1
        self.linkedlist.head = Node(None)
        self.linkedlist.tail = self.linkedlist.head

    def addOne(self, i):
        i = (i + 1) % self.maxlength
        return i

    def insertTail(self, ll, x):
        node = Node(x)
        ll.tail.next = node
        ll.tail = node

    def deleteHead(self, ll):
        if ll.head.next is None:
            return None

        node = ll.head.next
        ll.head.next = node.next
        if ll.head.next is None:
            ll.head = ll.tail

        return node.item

    def empty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, x):
        if self.addOne(self.addOne(self.rear)) == self.front:
            print("queue is full")
            return
        self.rear = self.addOne(self.rear)
        self.insertTail(self.linkedlist, x)
        self.size += 1

    def dequeue(self):
        if self.empty():
            print("queue is empty")
            return

        item = self.deleteHead(self.linkedlist)
        self.front = self.addOne(self.front)
        self.size -= 1
        return item

    def display(self):
        self.linkedlist.display()


myQueue = QueueLL(5)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)

print("Queue:")
myQueue.display()
print("Front:", myQueue.front)
print("Dequeue:", myQueue.dequeue())
print("Dequeue:", myQueue.dequeue())

print("Queue after Dequeue:")
myQueue.display()
myQueue.enqueue(5)
myQueue.enqueue(6)
print("Queue:")
myQueue.display()
print("isEmpty:", myQueue.empty())
print("Size:", myQueue.size)
