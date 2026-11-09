class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        res = []

        for x, y in points:
            dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        
        for _, x, y in heap:
            res.append([x, y])
        
        return res
        