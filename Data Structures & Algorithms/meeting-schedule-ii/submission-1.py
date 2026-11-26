"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort()
        start = []
        end = []

        for start, end in intervals:
            start.append(start)
            end.append(end)
        
        end.sort()
        i, j = 0, 0
        rooms = float("inf")
        res = 0

        while i < len(start):
            if start[i] < end[j]:
                rooms +=1
                i +=1
            else:
                rooms -=1
                j +=1
            
            rooms = max(rooms, res)
        return rooms
        

        