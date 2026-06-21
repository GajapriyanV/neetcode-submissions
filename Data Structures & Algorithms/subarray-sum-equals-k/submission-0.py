class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = {0 : 1}
        res = 0
        curSum = 0

        for num in nums:
            curSum += num

            if (curSum - k) in subs:
                res += subs[curSum - k]
            
            if curSum not in subs:
                subs[curSum] = 1
            else:
                subs[curSum] = subs.get(curSum, 0) + 1
        return res

        


        