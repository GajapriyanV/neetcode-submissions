class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            if len(heap) <= k:
                heapq.heappush(heap, nums)
            else:
                heapq.heappushpop(heap, nums)
        
        return heap[0]
        