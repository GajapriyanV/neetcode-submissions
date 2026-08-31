from _heapq import heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        self.nums = nums

        

    def add(self, val: int) -> int:
        heapq.heappushpop(self.nums, val)
        return self.nums[0]




        
