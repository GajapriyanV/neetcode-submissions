class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) > len(t):
            return ""
        
        sCount, tCount = defaultdict(int), defaultdict(int)

        for c in t:
            tCount[c] +=1
        
        match = 0
        l = 0
        minLen = len(s) - 1
        ansR, ansL = len(s), 0

        for r in range(len(s)):
            c = s[r]
            sCount[c] +=1

            if c in t and sCount[c] == tCount[c]:
                match +=1
            
            while match == len(tCount):
                sCount[s[l]] -=1

                if s[l] in t and sCount[s[l]] < tCount[s[l]]:
                    match -=1
                
                if (r - l + 1) < minLen:
                    ansR = r
                    ansL = l
                
                l +=1
        
        return s[ansL:ansR + 1]
        
        








        

        