class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            curSum = 0
            dayCount = 1

            for w in weights:
                if curSum + w <= capacity:
                    curSum += w
                else:
                    dayCount +=1
                    curSum = w
            
            return dayCount <= days
        

        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        

                    




        