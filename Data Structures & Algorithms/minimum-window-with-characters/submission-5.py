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
        

        for r in range(s):
            sCount[s[r]] +=1

            if r in tCount:
                if sCount[s[r]] == tCount[s[r]]:
                    match +=1
            
            while match == tmatch:
                res = min(res, (r - l) + 1)
                sCount[s[l]] -=1

                if sCount[s[l]] < tCount[s[l]]:
                    match -=1
                
                l +=1
        
        return res



        