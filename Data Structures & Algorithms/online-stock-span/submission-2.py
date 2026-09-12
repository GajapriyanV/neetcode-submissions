class StockSpanner:

    def __init__(self):

        self.stock = []
        

    def next(self, price: int) -> int:

        count = 1

        while self.stock and self.stock[-1][0] <= price:
            val, num = self.stock.pop()
            count += num
        
        self.stock.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)