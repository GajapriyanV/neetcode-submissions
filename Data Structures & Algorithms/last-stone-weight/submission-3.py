class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-x for x in stones]

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if second > first:
                heapq.heappush(max_heap, -(first - second))
        

        stones.append(0)
        return abs(stones[0])
        