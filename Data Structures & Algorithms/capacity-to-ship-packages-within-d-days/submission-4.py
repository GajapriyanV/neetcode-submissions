class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isCapacity(capacity):
            dayAmount = 1
            curWeight = 0

            for w in weights:
                if curWeight + w > capacity:
                    dayAmount +=1
                    curWeight = 0
                
                curWeight += w

            return dayAmount <= days
        

        l, r = 1, sum(weights)
        res = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if isCapacity(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res

