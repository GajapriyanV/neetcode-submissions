class StockSpanner:

    def __init__(self):
        self.spanner = []
        

    def next(self, price: int) -> int:
        span = 1

        while self.spanner and self.spanner[-1] <= price:
            span += self.spanner.pop()[1]
        
        self.spanner.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)