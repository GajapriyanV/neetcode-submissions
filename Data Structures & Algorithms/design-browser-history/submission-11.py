class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.history = [homepage]
        self.boundary = 0
        self.curIndex = 0

    def visit(self, url: str) -> None:
        if self.curIndex == len(self.history) - 1:
            self.history.append(url)
            self.boundary = self.curIndex + 1
        else:
            self.curIndex +=1
            self.history[self.curIndex] = url
            self.boundary = self.curIndex

    def back(self, steps: int) -> str:
        index = max(0, self.curIndex - steps)
        return self.history[index]


    def forward(self, steps: int) -> str:
        index = min(self.boundary, self.curIndex + steps)
        return self.history[index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)