class Node():
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

class linkedList():
    def __init__(self, head = None):
        self.head = head
    
    def removeNode(self,n):
        curNode = self.head
        for i in range(n-1):
            prevNode = curNode
            curNode = curNode.next
        
        prevNode.next = curNode.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)
lList = linkedList(node1)
lList.removeNode(2)

curNode = lList.head
while curNode!=None:
    print curNode.data
    curNode = curNode.next