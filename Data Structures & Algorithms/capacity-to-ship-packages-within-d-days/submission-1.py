class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def canShip(weight):
            days = 0
            curSum = 0

            for w in weights:
                if curSum + w > weight:
                    days +=1
                    curSum = 0
                
                curSum += w
            
            return days
        

        l, r = 0, sum(weights)
        res = 0

        while l <= r:
            mid = (l + r) // 2

            if canShip(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res

                
