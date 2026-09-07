class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        mapper = {0:1}
        res = 0
        curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - goal

            if diff in mapper:
                res += mapper[diff]
            
            mapper[curSum] = mapper.get(curSum, 0) + 1
        