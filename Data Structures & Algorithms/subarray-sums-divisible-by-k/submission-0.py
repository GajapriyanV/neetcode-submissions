class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        subCount = {0: 1}
        curSum = 0
        res = 0

        for num in nums:
            curSum += num
            diff = curSum % k
            res += subCount.get(diff, 0)

            if diff in subCount:
                subCount[diff] +=1
            else:
                subCount[diff] = 1
        
        return res
            

