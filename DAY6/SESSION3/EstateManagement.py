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
    
    def kthLargest(self, root, k):
        if root is None:
            return None
        
        right = self.kthLargest(root.right, k)
        if right is not None:
            return right
        
        k -= 1
        if k == 0:
            return root.data
        return self.kthLargest(root.left, k)

bt = BinaryTree()
bt.root = bt.insert(bt.root, 8)
bt.root = bt.insert(bt.root, 1)
bt.root = bt.insert(bt.root, 2)
bt.root = bt.insert(bt.root, 10)
bt.root = bt.insert(bt.root, 9)
print(bt.kthLargest(bt.root, 2))