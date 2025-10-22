
class Queue:
    def __init__(self, maxlength):
        self.maxlength = maxlength
        self.front = 0
        self.rear = self.maxlength - 1
        self.elements = [None for i in range(self.maxlength)]
        self.size = 0

    def addOne(self, i):
        i = (i + 1) % self.maxlength
        return i

    def makeNull(self):
        self.front = 0
        self.rear = self.maxlength - 1
        self.elements = [None for i in range(self.maxlength)]
        self.size = 0

    def empty(self):
        if self.addOne(self.rear) == self.front:
            return True

        return False

    def Front(self):
        if self.empty():
            print("queue is empty")
            return
        return self.elements[self.front]

    def enqueue(self, x):
        if self.addOne(self.addOne(self.rear)) == self.front:
            print("queue is full")
            return
        self.rear = self.addOne(self.rear)
        self.elements[self.rear] = x
        self.size += 1

    def dequeue(self):
        if self.empty():
            print("queue is empty")
            return

        item = self.elements[self.front]
        self.front = self.addOne(self.front)
        self.size -= 1
        return item


myQueue = Queue(5)
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')

print("Queue", myQueue.elements)
print("Front:", myQueue.front)
print("Dequeue:", myQueue.dequeue())
print("Dequeue:", myQueue.dequeue())

print("Queue after Dequeue:", myQueue.elements)
myQueue.enqueue('X')
myQueue.enqueue('Y')
print("Queue", myQueue.elements)
print("isEmpty:", myQueue.empty())
print("Size:", myQueue.size)
