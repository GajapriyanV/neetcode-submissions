class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup = set()

        for num in nums:
            if num in dup:
                return False
            dup.add(num)
        
        return True
        