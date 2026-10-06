class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self.removeNode(node)
            self.addNode(node)
        else:
            newNode = ListNode(key, value)
            self.keyToNode[key] = newNode
            self.addNode(newNode)

            if self.capacity > 0:
                self.capacity -=1
            else:
                key = self.removeLRU()
                del self.keyToNode[key]



    
    def addNode(self, newNode):
        lastNode = self.tail.prev
        lastNode.next = newNode
        newNode.next = self.tail
        newNode.prev = lastNode
        self.tail.prev = newNode
    
    def removeNode(self, removeNode):
        previous, nextNode = removeNode.prev, removeNode.next
        previous.next = nextNode
        nextNode.prev = previous
    
    def removeLRU(self):
        lruNode = self.head.next
        self.removeNode(lruNode)
        return lruNode.key

    

        
