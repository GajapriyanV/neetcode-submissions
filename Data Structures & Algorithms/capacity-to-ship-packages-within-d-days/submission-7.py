class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(weight):
            taken = 0
            curWeight = 0

            for w in weights:
                curWeight += w

                if curWeight > weight:
                    taken +=1
                    curWeight = w
            
            taken +=1

            return taken <= days
        

        l, r = max(weights), sum(weights)
        res = float("inf")

        while l <= r:

            mid = (l + r) // 2

            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res


        