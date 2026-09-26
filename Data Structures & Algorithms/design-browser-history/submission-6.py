class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        # Remove any forward history
        self.browser = self.browser[:self.idx + 1]

        self.browser.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.browser[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.browser) - 1, self.idx + steps)
        return self.browser[self.idx]