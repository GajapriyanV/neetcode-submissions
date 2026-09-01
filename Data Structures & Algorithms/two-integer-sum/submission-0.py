class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        occur = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in occur:
                ans = occur[diff]
                return [i, ans]
            else:
                occur[diff] = i
        
        