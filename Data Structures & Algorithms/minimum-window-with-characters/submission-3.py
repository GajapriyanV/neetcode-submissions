class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tCount = defaultdict(int)
        sCount = defaultdict(int)
        match = 0
        res = float("infinity")
        

        for c in t:
            tCount[c] +=1

        tmatch = len(tCount)
        l = 0
        

        for r in s:
            sCount[r] +=1

            if r in tCount:
                if sCount[r] == tCount[r]:
                    match +=1
            
            while match == tmatch:
                res = min(res, r - l + 1)
                sCount[l] -=1

                if sCount[l] < tCount[l]:
                    match -=1
                
                l +=1
        
        return res



        