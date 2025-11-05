
from LinkedList import LinkedList, Node

class QueueLL:
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.front = 0
        self.rear = self.maxlength - 1
        self.size = 0
        self.linkedList = LinkedList()

    def addOne(self, item):
        item = (item + 1) % self.maxlength

        return item
    
    def makeNull(self):
        self.front = 0
        self.rear = self.maxlength - 1
        self.size = 0
        self.linkedList = LinkedList()

    def insertTail(self, x):
        node = Node(x)
        self.linkedList.tail.next = node
        self.linkedList.tail = node

    def deleteHead(self):
        if self.linkedList.head.next is None:
            return None
        
        node = self.linkedList.head.next
        self.linkedList.head.next = node.next
        if self.linkedList.head.next is None:
            self.linkedList.head = self.linkedList.tail

        return node.item
    
    def empty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, x):
        if self.addOne(self.addOne(self.rear)) == self.front:
            return "Queue is full"
        
        self.rear = self.addOne(self.rear)
        self.insertTail(x)
        self.size += 1

    def dequeue(self):
        if self.empty():
            return "Queue is empty"
        
        item = self.deleteHead()
        self.front = self.addOne(self.front)
        self.size -= 1

        return item
    
    def display(self):
        self.linkedList.display()
        



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

