import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calc_hours(rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
        
            return hours

        l, r = 0, max(piles)
        while l < r:

            mid = (l + r) // 2

            if calc_hours(mid) <= h:
                r = mid
            else:
                l = mid + 1
        
        return l


        