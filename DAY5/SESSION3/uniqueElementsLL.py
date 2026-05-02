class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def uniqueElements(self):
        curr = self.head
        s = []
        prev = None
        while curr:
            if curr.data not in s:
                s.append(curr.data)
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
            

    def printNodes(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(f"{curr.data} -> ", end="")
            curr = curr.next
        print("None\n")

l = linkedList()
l.insertAtEnd(1001)
l.insertAtEnd(1002)
l.insertAtEnd(1003)
l.insertAtEnd(1002)
l.insertAtEnd(1004)
l.insertAtEnd(1003)
l.printNodes()
l.uniqueElements()
l.printNodes()