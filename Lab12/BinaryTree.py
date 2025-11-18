
class BTree:
    def __init__(self, item):
        self.data = item
        self.lc = None
        self.rc = None
    
    def addlc(self, item):
        assert self.lc is None, "Left child is already present"
        self.lc = BTree(item)

    def addrc(self, item):
        assert self.rc is None, "Right child is already present"
        self.rc = BTree(item)

    def dellc(self):
        assert self.lc is not None, "Left child absent"
        assert self.lc.lc is None and self.lc.rc is None, "This node has children"

        x = self.lc.data
        self.lc = None
        return x
    
    def delrc(self):
        assert self.rc is not None, "Right child absent"
        assert self.rc.lc is None and self.rc.rc is None, "This node has children"

        x = self.rc.data
        self.rc = None
        return x
    
    def height(self):
        if self.rc is None and self.lc is None:
            return 1
        
        rh = 0
        lh = 0
        if self.rc is not None:
            rh = self.rc.height()
        
        if self.lc is not None:
            lh = self.lc.height()
        
        if rh > lh:
            return rh + 1
        return lh + 1
    
    def TreeSize(self):  #Node Count function
        if self.lc is None and self.rc is None:
            return 1
        
        lnc = 0
        rnc = 0

        if self.lc is not None:
            lnc = self.lc.TreeSize()
        
        if self.rc is not None:
            rnc = self.rc.TreeSize()
        
        return lnc + rnc + 1
    
    def clearTree(self):
        if self.lc is None and self.rc is None:
            self.data = 0
            return

        if self.lc is not None:
            self.lc.data = 0
            self.lc.clearTree()
        
        if self.rc is not None:
            self.rc.data = 0
            self.rc.clearTree()

        self.data = 0

    def traverseInOrder(self):
        if self.lc is not None:
            self.lc.traverseInOrder()

        print(self.data, end = " ")

        if self.rc is not None:
            self.rc.traverseInOrder()

    def traversePreOrder(self):
        
        print(self.data, end = " ")

        if self.lc is not None:
            self.lc.traversePreOrder()

        if self.rc is not None:
            self.rc.traversePreOrder()

    def traversePostOrder(self):

        if self.lc is not None:
            self.lc.traversePostOrder()

        if self.rc is not None:
            self.rc.traversePostOrder()

        print(self.data, end = " ")

    def doubleOrderTraversal(self):
        
        print(self.data, end=" ")

        if self.lc is not None:
            self.lc.doubleOrderTraversal()
        
        print(self.data, end=" ")

        if self.rc is not None:
            self.rc.doubleOrderTraversal()
        

if __name__ == "__main__":
    root = BTree(1)
    root.addrc(2)
    root.rc.addlc(3)
    root.rc.lc.addrc(5)
    root.rc.lc.addlc(4)

    print("InOrder Traversal:", end=" ")
    root.traverseInOrder()
    print()

    print("PreOrder Traversal:", end=" ")
    root.traversePreOrder()
    print()

    print("PostOrder Traversal:", end=" ")
    root.traversePostOrder()
    print()

    print("Double Order Traversal:", end=" ")
    root.doubleOrderTraversal()
    print()

    print("Clear Tree:", end=" ")
    root.clearTree()
    print()

    print("Traverse:", end=" ")
    root.traversePreOrder()
    print()

