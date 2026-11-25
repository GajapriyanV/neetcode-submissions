class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(limit):
            subarrays = 1
            currSum = 0

            for num in nums:
                if currSum + num > limit:
                    subarrays += 1
                    currSum = num
                else:
                    currSum += num

            return subarrays <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left