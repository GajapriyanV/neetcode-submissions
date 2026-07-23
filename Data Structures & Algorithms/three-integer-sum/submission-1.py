class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:

                curSum = nums[i] + nums[l] + nums[r]

                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    if l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l +=1
                    if r - 1 > 0 and nums[r] == nums[r -1]:
                        r-=1
                
                if curSum > 0:
                    r -=1
                if curSum < 0:
                    l +=1
        
        return res

        