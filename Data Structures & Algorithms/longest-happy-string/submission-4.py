
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []

        heap = [(-count, char) for count, char in
                [(a, "a"), (b, "b"), (c, "c")] if count > 0]
        heapq.heapify(heap)

        prev = None

        while heap:
            count, char = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                prev = (count, char)
                continue
            else:
                res.append(char)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, char))

            if prev:
                heapq.heappush(heap, prev)
                prev = None

        return "".join(res)
