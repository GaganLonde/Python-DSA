class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def printBT(self, root):
        if root is None:
            return
        self.printBT(root.left)
        print(root.data)
        self.printBT(root.right)

    def largest(self, root):
        
        if root.right is None:
            return root.data
        return self.largest(root.right)

bt = BinaryTree()
bt.root = bt.insert(bt.root, 1)
bt.root = bt.insert(bt.root, 2)
bt.root = bt.insert(bt.root, 3)
bt.root = bt.insert(bt.root, 10)
bt.root = bt.insert(bt.root, 4)
bt.printBT(bt.root)
print("Largest: ", bt.largest(bt.root))