class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0

        numCheck = set(nums)

        for num in nums:
            if num - 1 not in numCheck:
                curLen = 0
                while num in numCheck:
                    num +=1
                    curLen +=1
                
                longest = max(longest, curLen)
        
        return longest

        