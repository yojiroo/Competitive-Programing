class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def addMany(self,values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeDuplicatesFromLinkedList(linkedList):
    #print(linkedList.getNodesInArray())
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        #print(currentNode.value)
        #print(nextDistinctNode.value)
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode    
        currentNode = nextDistinctNode
        #print(currentNode.getNodesInArray())
        #print(currentNode.next.getNodesInArray())
        #print(linkedList.getNodesInArray())
        #print(linkedList.next.getNodesInArray())
    return linkedList

test = LinkedList(1).addMany([1,3,4,4,4,5,6,6])
a  = removeDuplicatesFromLinkedList(test)
print(a.getNodesInArray())