class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        res = []

        def dfs(target):

            if target == 0:
                return 1
            
            ans = 0
            for num in nums:
                diff = target - num
                if diff >= 0:
                    ans += dfs(diff)
            
            return ans
            
        
        return dfs(target)
                

        