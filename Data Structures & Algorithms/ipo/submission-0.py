import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            # Add all projects we can currently afford
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1

            # No affordable projects remaining
            if not maxHeap:
                break

            # Complete the most profitable project
            w += -heapq.heappop(maxHeap)

        return w