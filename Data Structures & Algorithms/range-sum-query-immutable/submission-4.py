class NumArray:

    def __init__(self, nums: List[int]):

        prefixSum = []
        curSum = 0
        for num in nums:
            curSum += num
            prefixSum.append(curSum)
        
        self.nums = prefixSum
        self.total = curSum

        

    def sumRange(self, left: int, right: int) -> int:

        left = self.nums[left - 1] if left - 1 > 0 else 0
        right = self.nums[right]
        return right - left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)