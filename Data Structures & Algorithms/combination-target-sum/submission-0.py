class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        cur = []


        def dfs(i, target):

            if i >= len(nums) or target < 0:
                return

            if target == 0:
                res.append(cur.copy())
                return
            
            
            cur.append(nums[i])
            dfs(i, target - nums[i])
            cur.pop()
            dfs(i + 1, target)

        
        return res
            


        