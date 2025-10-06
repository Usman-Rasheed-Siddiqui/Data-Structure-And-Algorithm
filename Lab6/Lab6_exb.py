
class Node:
    def __init__(self, value):
        self.left = None
        self.item = value
        self.right = None

class DoublyLinkedList:
    def __init__(self, value):
        self.node = Node(value)

    def __len__(self):
        a = self.node
        sum = 0
        while a is not None:
            sum += 1
            a = a.left

        a = self.node.right
        while a is not None:
            sum += 1
            a = a.right

        return sum

    def display(self):
        node = self.node

        while node and node.left is not None:
            node = node.left
        print("None", end = " <-> ")
        while node is not None:
            print(node.item, end=" <-> ")
            node = node.right
        if node is None:
            print(node)    

    def insertright(self, value):
        q = self.node
        r = self.node.right
        node = Node(value)

        if q is not None:
            q.right = node
            if r is not None:
                r.left = node

            node.left = q
            node.right = r

    def insertleft(self, value):
        
        p = self.node.left
        q = self.node

        node = Node(value)

        if q is not None:
            q.left = node
            if p is not None:
                p.right = node
            
            node.right = q
            node.left = p

    
    def search(self, value):
        q = self.node

        while q is not None and q.item != value:
            q = q.left

        if q is not None:
            return q
        
        q = self.node.right

        while q is not None and q.item != value:
            q = q.right

        if q is not None:
            return q

        return None
    
    def delete(self, target):

        p = self.node.left
        q = self.node
        r = self.node.right

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
        

dl = DoublyLinkedList(20)
print("Insertion: ")
dl.insertright(10)
dl.insertleft(9)
dl.insertright(11)
dl.insertleft(8)
dl.display()
print("Searching: ")
print(dl.search(9))
print("Deletion:")
dl.delete(8)
dl.display()