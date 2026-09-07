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

        return self.total - self.nums[left - 1] - self.nums[right + 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)