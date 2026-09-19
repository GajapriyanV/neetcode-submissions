class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        res = []
        cur = []

        def dfs(target):

            if target == 0:
                res.append(cur.copy())
                return
            

            for num in nums:
                diff = target - num
                if diff >= 0:
                    dfs(diff)
            
        
        return res
                

        