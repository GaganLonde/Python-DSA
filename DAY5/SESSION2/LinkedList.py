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

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev

    def printNodes(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(f"{curr.data} -> ", end="")
            curr = curr.next
        print("None\n")
            
    def swap(self, data1, data2):
        if data1 == data2:
            return
        currX, currY = self.head, self.head
        prevX, prevY = None, None
        while currX and currX.data != data1:
            prevX = currX
            currX = currX.next
        while currY and currY.data != data2:
            prevY = currY
            currY = currY.next

        if not currX or not currY:
            return
        
        if prevX:
            prevX.next = currY
        else:
            head = currY

        if prevY:
            prevY.next = currX
        else:
            head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

l = linkedList()
l.insertAtEnd(1)
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(4)
l.insertAtEnd(5)
l.printNodes()
l.reverse()
l.printNodes()
l.swap(4, 2)
l.printNodes()


