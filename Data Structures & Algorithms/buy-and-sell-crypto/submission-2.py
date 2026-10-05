class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxRes = 0

        l = 0

        for r in range(len(prices)):

            if prices[l] < prices[r]:
                maxRes = max(maxRes, prices[r] - prices[l])
            else:
                l = r
        
        return maxRes