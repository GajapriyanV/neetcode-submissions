class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            prevEnd = res[-1][1]
            curStart = intervals[i][0]
            curEnd = intervals[i][1]

            if curStart <= prevEnd:
                res[-1][1] = max(prevEnd, curEnd)
            else:
                res.append(intervals[i])
        
        return res


        