
class Node:
    def __init__(self, value):
        self.left = None
        self.item = value
        self.right = None

class DoublyLinkedList:
    def __init__(self, value):
        self.node = Node(value)

    def __len__(self):
        
        a = self
        sum = 0

        while a is not None:
            sum += 1
            a = a.left

        a = self.left

        while a is not None:
            sum += 1
            a = a.right

        return sum
    
    def insertright(self, value):
        q = self
        r = self.right
        node = Node(value)

        if q is not None:
            q.right = node
            if r is not None:
                r.left = node

            node.left = q
            node.right = r

    def insertleft(self, value):
        
        p = self.left
        q = self

        node = Node(value)

        if q is not None:
            q.left = node
            if p is not None:
                p.right = node
            
            node.right = q
            node.left = p

    def search(self, value):
        q = self

        while q is not None and q.item != value:
            q = q.left

        if q is not None:
            return q
        
        q = self.right

        while q is not None and q.item != value:
            q = q.right

        if q is not None:
            return q

    
    def delete(self, target):

        p = self.left
        q = self
        r = self.right

        if q.item == target:
            if p is not None:
                p.right = r
            
            if r is not None:
                r.left = p
            
            return q

        if p is not None and p.item != target:
            p = p.left
        
        if p is not None:
            r = p.right
            q = p
            p = p.left

            p.right = r
            r.left = p

            return q
        
        if r is not None and r.item != target:
            r = r.right
        
        if r is not None:
            p = r.right
            q = r
            r = r.left

            p.right = r
            r.left = p

            return q
        
    def display(self):
        node = self

        if node is not None:
            node = node.left

        while node is not None:
            print(node, end=" <-> ")
            node = node.right
            if node is None:
                print(node)

