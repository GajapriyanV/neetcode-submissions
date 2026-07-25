class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:

            if len(heap) > k:
                heapq.heappushpop(heap, nums)
                heapq.heappush(heap, nums)
            else:
                heapq.heappush(heap, nums)
        
        return heap[0]
        