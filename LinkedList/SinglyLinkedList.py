
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insert(self, value):
        x = ListNode(value)
        x.next = self.next
        self.next = x
    
    def delete(self):
        item = None
        if self.next is not None:
            temp = self.next
            self.next = temp.next
            item = temp.data
        
        return item
    
    def __len__(self):
        a = self
        i = 0
        while a is not None:
            a = a.next
            i += 1

        return i
    
    def traverse(self):
        a = self
        print("\nTraverse in the list: ")
        while a is not None:
            print(a.data, end=" ")
            a = a.next

    def search(self, target):
        a = self
        if a.data == target:
            return [True, None, a]
        
        b = a.next

        while b is not None and b.data != target:
            a = a.next
            b = b.next
        
        return [b is not None, a, b]
    
    def circularize(self):
        a = self
        while a.next is not None:
            a = a.next

        a.next = self
    
    def linearize(self):
        a = self
        while a.next is not self:
            a = a.next

        a.next = None
    
    def traverseCircular(self):
        a = self
        print("\nTraverse Circular List:")
        while True:
            print(a.data, end = " -> ")
            a = a.next
            if a is self:
                print(f"({a.data}) #back to start")
                break
        

# Create first node
head = ListNode(10)

# Test 1: Insert a few nodes
head.insert(20)     # List: 10 -> 20
head.insert(30)     # List: 10 -> 30 -> 20
head.insert(40)

head.traverse()
head.circularize()
head.traverseCircular()
