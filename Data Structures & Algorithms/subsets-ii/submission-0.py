class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        cur = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            while i - 1 > 0 and nums[i] == nums[i - 1]:
                i +=1
            
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
        