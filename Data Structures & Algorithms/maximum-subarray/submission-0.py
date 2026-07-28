class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        themax = float("-infinity")
        cur = 0

        for num in nums:
            cur += num
            themax = max(themax, cur)

            if cur < 0:
                cur = 0
        
        return int(themax)

        