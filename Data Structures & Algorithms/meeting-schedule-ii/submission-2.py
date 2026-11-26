class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        i, j = 0, 0
        rooms = 0
        res = 0

        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1

            res = max(res, rooms)

        return res