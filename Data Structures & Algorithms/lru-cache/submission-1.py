class ListNode:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyStore = {}

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.keyStore:
            return -1

        node = self.keyStore[key]

        # Move it to MRU position
        self.removeNode(node)
        self.addNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyStore:
            node = self.keyStore[key]
            node.val = value

            self.removeNode(node)
            self.addNode(node)

        else:
            newNode = ListNode(key, value)

            self.keyStore[key] = newNode
            self.addNode(newNode)

            if len(self.keyStore) > self.capacity:
                self.removeLRU()

    def addNode(self, node):
        # Add right before tail = most recently used
        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def removeLRU(self):
        # Node right after head = least recently used
        lru = self.head.next

        self.removeNode(lru)
        del self.keyStore[lru.key]