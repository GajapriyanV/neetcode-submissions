class NumArray:

    def __init__(self, nums: List[int]):

        prefixSum = []
        curSum = 0
        for num in nums:
            curSum += num
            prefixSum.append(curSum)

        

    def sumRange(self, left: int, right: int) -> int:
        
        totalSum = prefixSum[-1]

        return totalSum - prefixSum[l - 1] - prefixSum[r + 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)