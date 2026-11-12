
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adjMap = defaultdict(list)
        for start, dest, w in flights:
            adjMap[start].append((dest, w))

        heap = [(0, src, -1)]
        best = {(src, -1): 0}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if cost > best[(node, stops)]:
                continue

            if node == dst:
                return cost

            if stops == k:
                continue

            for nei, w in adjMap[node]:
                newCost = cost + w
                newStops = stops + 1

                if newCost < best.get((nei, newStops), float("inf")):
                    best[(nei, newStops)] = newCost
                    heapq.heappush(heap, (newCost, nei, newStops))

        return -1
