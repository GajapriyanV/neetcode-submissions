class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def permute(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):

                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                nums[i], nums[j] = nums[j], nums[i]
                permute(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
        
        
        permute(0)
        return res