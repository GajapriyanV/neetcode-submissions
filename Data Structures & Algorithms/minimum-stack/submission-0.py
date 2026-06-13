class MinStack:

    def __init__(self):
        
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        
        if self.minStack:
            self.stack.append(val)
            local_min = min(val, self.minStack[-1])
            self.minStack.append(local_min)
        else:
            self.stack.append(val)
            self.minStack.append(val)
        

    def pop(self) -> None:

        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()