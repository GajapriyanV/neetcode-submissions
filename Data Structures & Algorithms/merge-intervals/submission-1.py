class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(intervals[i])
        
        return res
        