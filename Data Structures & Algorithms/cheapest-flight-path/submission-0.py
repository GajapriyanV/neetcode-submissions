
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adjMap = defaultdict(list)
        for start, dest, w in flights:
            adjMap[start].append((dest, w))

        heap = [(0, src, -1)]  # cost, node, stops

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if stops > k:
                continue

            if node == dst:
                return cost

            for nei, w in adjMap[node]:
                heapq.heappush(heap, (cost + w, nei, stops + 1))

        return -1
