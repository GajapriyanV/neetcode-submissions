class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:  # Check if the sum is odd
            return False

        target = sum(nums) // 2
        n = len(nums)

        # Initialize the memo table with dimensions (n + 1) x (target + 1)
        memo = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            memo[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                take = False
                if j >= nums[i]:
                    take = memo[i - 1][j - nums[i - 1]]
                
                notTake = memo[i - 1][j]

                memo[i][j] = take or notTake
        
        return memo[n][target]
                

