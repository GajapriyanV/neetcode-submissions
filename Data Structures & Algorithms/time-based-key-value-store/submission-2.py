from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]

        l, r = 0, len(values) - 1
        mid = (l + r) // 2
        mid_timestamp, mid_value = values[mid]
        res = ""

        while l <= r:

            if mid_timestamp <= timestamp:
                res = mid_value
                l = mid + 1
            else:
                r = mid - 1
        
        return res


            
        
        

            

        