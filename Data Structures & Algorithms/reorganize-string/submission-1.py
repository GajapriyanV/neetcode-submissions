
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = defaultdict(int)
        res = []

        for c in s:
            charCount[c] += 1

        maxHeap = []

        for letter, count in charCount.items():
            heapq.heappush(maxHeap, (-count, letter))

        toAdd = None

        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            res.append(letter)
            count += 1

            if toAdd:
                heapq.heappush(maxHeap, toAdd)

            toAdd = (count, letter) if count < 0 else None

        return "".join(res) if len(res) == len(s) else ""
