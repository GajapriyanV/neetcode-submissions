class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.browser = self.browser[:self.idx + 1]
        self.browser.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        if self.idx - steps >= 0:
            self.idx = self.idx - steps
        else:
            self.idx = 0

        return self.browser[self.idx]

    def forward(self, steps: int) -> str:
        if self.idx + steps <= len(self.browser) - 1:
            self.idx = self.idx + steps
        else:
            self.idx = len(self.browser) - 1

        return self.browser[self.idx]