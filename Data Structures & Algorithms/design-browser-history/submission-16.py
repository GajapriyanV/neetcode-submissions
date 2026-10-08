class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.history = [homepage]
        self.boundary = 0
        self.curIndex = 0

    def visit(self, url: str) -> None:
        self.curIndex +=1
        if self.curIndex == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curIndex] = url
        
        self.boundary = self.curIndex

    def back(self, steps: int) -> str:
        self.curIndex = max(0, self.curIndex - steps)
        return self.history[self.curIndex]


    def forward(self, steps: int) -> str:
        self.curIndex = min(self.boundary, self.curIndex + steps)
        return self.history[self.curIndex]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)