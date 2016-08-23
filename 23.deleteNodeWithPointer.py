class LinkedList():

    class Node():
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
    
    def push(self,data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def delete(self,Node):
        temp = Node.next
        Node.data = temp.data
        Node.next = temp.next
        temp = None
        
    def printList(self):
        curNode = self.head
        while curNode != None:
            print curNode.data
            curNode = curNode.next
        
lst = LinkedList()
lst.push('1')
lst.push('10')
lst.push('ok')
lst.push('head')
#lst.printList()
lst.delete(lst.head)
lst.printList()