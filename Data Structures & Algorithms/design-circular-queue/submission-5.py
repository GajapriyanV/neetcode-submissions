class ListNode:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k          
        self.size = k              

        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        # Queue is full
        if self.isFull():
            return False

        newNode = ListNode(value)

        # Insert before tail
        lastQueued = self.tail.prev

        lastQueued.next = newNode
        newNode.prev = lastQueued

        newNode.next = self.tail
        self.tail.prev = newNode

        self.capacity -= 1

        return True

    def deQueue(self) -> bool:
        # Queue is empty
        if self.isEmpty():
            return False

        # Remove first node
        toRemove = self.head.next
        newHead = toRemove.next

        self.head.next = newHead
        newHead.prev = self.head

        self.capacity += 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.capacity == self.size

    def isFull(self) -> bool:
        return self.capacity == 0