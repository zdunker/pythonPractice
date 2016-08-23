class linkedList():
    def __init__(self,head = None):
        self.head = head
    def printList(self):
        curNode = self.head
        while curNode != None:
            print curNode.data
            curNode = curNode.next
    
    def push(self,newNode):
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode
    
    def reverseList(self):
        curNode = self.head
        previous = None
        while curNode.next != None:
            tmpNode = curNode.next
            curNode.next = previous
            previous = curNode
            curNode = tmpNode
        curNode.next = previous
        self.head = curNode
            
class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,next):
        self.next = next

if __name__ == '__main__':
    headNode = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)
    headNode.setNext(secondNode)
    lst = linkedList(headNode)
    lst.push(thirdNode)
    lst.printList()
    #print lst.head.data
    lst.reverseList()
    lst.printList()