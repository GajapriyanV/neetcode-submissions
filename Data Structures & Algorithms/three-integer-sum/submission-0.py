class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1] or a > 0:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r] + a
                if cur_sum > 0:
                    r = r - 1
                elif cur_sum < 0:
                    l = l + 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                    while nums[r] == nums[r + 1] and l < r:
                        r-=1
        
        return res

                






        
        