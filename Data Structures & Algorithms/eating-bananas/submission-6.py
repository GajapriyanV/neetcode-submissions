class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTime(rate):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / rate)
                
            
            return totalTime
        

        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            timeTaken = calculateTime(mid)

            if timeTaken <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l