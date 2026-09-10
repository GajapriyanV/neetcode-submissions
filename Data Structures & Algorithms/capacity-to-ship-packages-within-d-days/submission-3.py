class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            daysUsed = 1
            curSum = 0

            for w in weights:
                if curSum + w > capacity:
                    daysUsed += 1
                    curSum = 0

                curSum += w

            return daysUsed <= days

        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2

            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res