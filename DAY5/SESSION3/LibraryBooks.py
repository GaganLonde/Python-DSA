class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:

    def __init__(self):
        self.head = Node(None)

    def inserDLL(self, data):
        if self.head == None:
            newNode = Node(data)
            newNode.next = self.head
            newNode.prev = self.head
            self.head = newNode

        curr = self.head
        while curr.next:
            curr = curr.next

        newNode = Node(data)
        newNode.next = None
        newNode.prev = curr
        curr.next = newNode

    def printDLL(self):
        if not self.head:
            return
        curr = self.head
        while curr:
            print(f"{curr.data} -> ", end="")
            curr = curr.next
        print("None\n")

        curr = self.head
        while curr.next:
            curr = curr.next
        
        while curr:
            print(f"{curr.data} -> ", end="")
            curr = curr.prev
        print("None\n")

arr = ["apple", "banana", "c++", "java", "python"]


l = doublyLinkedList()
for data in arr:
    l.inserDLL(data)

l.printDLL()

    