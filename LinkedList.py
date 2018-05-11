
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, item):
        current = self.head
        previous = None
        
        while current != None:
            if current.getData() > item:
                break
            else:
                previous = current
                current = current.getNext()
                
        temp = SListNode(item)
        
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def remove(self, item):
        current = self.head
        previous = None
        
        while current.getData() != None:
            if current.getData() == item:
                break
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    
    def contains(self, item):
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
        return found
    
    def items(self):
        items = []
        current = self.head
        while current != None:
            items.append(current.getData())
            current = current.getNext()
        return items

        
class SListNode:
    def __init__(self, data=None):
        self.data = data
        self.successor = None  # next item in list
        
    def getNext(self):
        return self.successor
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
        
    def setNext(self, nextNode):
        self.successor = nextNode
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.successor = None  # next item in list
        self.predecessor = None  # previous item in list