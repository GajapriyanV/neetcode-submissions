class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            leftSum += nums[i]
            rightSum = total - leftSum
            if leftSum == rightSum:
                return i
        
        return -1

        