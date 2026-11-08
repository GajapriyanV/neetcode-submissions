class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap = []
        for num in arr:
            diff = abs(num - x)
            heapq.heappush(heap, (diff, num))

            if len(heap) >= k:
                heapq.heappop(heap)
        
        
        res = []
        for _ , num in heap:
            res.append(num)
        
        return res

        