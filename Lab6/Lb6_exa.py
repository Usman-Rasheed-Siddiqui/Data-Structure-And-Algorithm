
class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next
    
    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next
    
    def setItem(self, item):
        self.item = item

    def setNext(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
 
    def __len__(self):
        size = 0
        b = self.head.next
        while b is not None:
            b = b.next
            size += 1
        
        return size

    def insert(self, value, index):

        node = Node(value)
        cursor = self.head
        
        size = len(self)
        
        if index <= size:
            for i in range(index):
                cursor = cursor.next

            node.next = cursor.next
            cursor.next = node
        
        else:
            for i in range(size):
                cursor = cursor.next
            
            node.next = cursor.next
            cursor.next = node

        if node.next is None:
            self.tail = node

    def search(self, target):
        N = self.head.next
        while N is not None:
            if N.item == target:
                return N
            N = N.next

        return None

    def delete(self, target):
        size = len(self)

        if size == 1:
            self.head.next = None
            self.head = self.tail
            return 
        
        precursor = self.head
        cursor = self.head.next

        while cursor is not None:
            if cursor.item == target:
                precursor.next = cursor.next

                if cursor.next is None:
                    self.tail = precursor

                return

            else:
                precursor = cursor
                cursor = cursor.next

    def display(self):
        current = self.head
        while current:
            print(current.item, end = " -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.display()
ll.insert(10, 0)   # [10]
ll.insert(20, 1)   # [10, 20]
ll.display()
print(ll.search(10).next)
ll.insert(15, 1)   # [10, 15, 20]
ll.insert(30, 100) # large index -> append at end [10, 15, 20, 30]
ll.display()
ll.delete(15)
ll.display()

