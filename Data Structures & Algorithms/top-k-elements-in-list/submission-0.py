class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqCount = Counter(nums)

        freqMap = [[] for i in range(len(nums) + 1)]

        res = []

        for count in range(len(freqMap), -1, -1):
            for num in freqMap[count]:
                res.append(nums)
                if len(res) >= k:
                    return res

        