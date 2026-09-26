class BrowserHistory:

    def __init__(self, homepage: str):

        self.browser = [homepage]
        self.idx = 0
        

    def visit(self, url: str) -> None:

        self.browser.append(url)
        self.idx = len(self.browser) - 1
        

    def back(self, steps: int) -> str:

        if (self.idx + 1) - steps >= 0:
            return self.browser[self.idx]
        else:
            return self.browser[0]

        

    def forward(self, steps: int) -> str:

        if self.idx + steps <= len(self.browser):
            return self.browser[self.idx]
        else:
            return self.browser[len(self.browser) - 1]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)