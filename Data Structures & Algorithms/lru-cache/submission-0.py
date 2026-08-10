class Node:
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):

        self.indexToNode = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev
    

    def add(self, node):

        endNode = self.tail.prev
        endNode.next = node
        node.prev = endNode
        node.next = self.tail
        self.tail.prev = node

        
    def get(self, key: int) -> int:

        if key in self.indexToNode:
            node = self.indexToNode[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:

        if key in self.indexToNode:
            node = self.indexToNode[key]
            node.value = value
            self.remove(node)
            self.add(node)

        else:
            newNode = Node(key, value)
            self.indexToNode[key] = newNode
            self.add(newNode)

            if len(self.indexToNode) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.indexToNode[lru.key]