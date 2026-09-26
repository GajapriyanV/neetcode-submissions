class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k

        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        firstEl = self.head.next
        newEl = ListNode(value)

        newEl.next = firstEl
        newEl.prev = self.head

        firstEl.prev = newEl
        self.head.next = newEl

        self.cap -= 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        lastEl = self.tail.prev
        secondLastEl = lastEl.prev

        secondLastEl.next = self.tail
        self.tail.prev = secondLastEl

        self.cap += 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.prev.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.val

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.cap == 0