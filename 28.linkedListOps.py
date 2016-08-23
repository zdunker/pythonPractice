class linkedList():
    class Node():
        def __init__(self,data):
            self.data = data
            self.next = None
            
    def __init__(self): 
        self.head = None
    
    def printList(self):
        curNode = self.head
        while curNode != None:
            print curNode.data
            curNode = curNode.next
    
    def push(self,data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def removeWithData(self,data):
        curNode = self.head
        while curNode.next != None:
            if curNode.next.data == data:
                curNode.next = curNode.next.next
                return
            curNode = curNode.next
        print "Node with %s not found"%(data)
    
    def removeWithPtr(self,tarNode):
        tmp = tarNode.next
        tarNode.data = tmp.data
        tarNode.next = tmp.next
        tmp = None
        
    def swapNodes(self,node1,node2):
        tmp1 = node1
        tmp2 = node2
        node1.data = tmp2.data
        #node1.next = tmp2.next
        node2.data = tmp1.data
        #node2.next = tmp1.next
        tmp1 = None
        tmp2 = None
    
if __name__ == '__main__':
    lst = linkedList()
    lst.push('hello')
    lst.push('my')
    lst.push('name')
    lst.push('is')
    lst.push('robin')
    lst.push('robin')
    lst.printList()
    lst.removeWithData('robin')
    lst.removeWithData('raa')
    lst.swapNodes(lst.head.next.next, lst.head)
    lst.printList()