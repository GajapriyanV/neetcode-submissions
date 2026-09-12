class StockSpanner:

    def __init__(self):

        self.stock = []
        

    def next(self, price: int) -> int:

        count = 1

        while self.stack and self.stack[-1][0] <= price:
            val, num = self.stack.pop()
            count += num
        
        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)