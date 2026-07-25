class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if not s1 or s2:
            return False
        
        charCount1 = [0] * 26
        charCount2 = [0] * 26

        for i in range(min(len(s1), len(s2))):
            charCount1[ord(s1[i]) - ord("a")] +=1
            charCount2[ord(s1[i]) - ord("a")] +=1
        
        if charCount1 == charCount2:
            return True
        
        l = len(s1)
        for j in range(len(s1), len(s2)):
            charCount2[ord(s1[j]) - ord("a")] +=1
            charCount2[ord(s1[l]) - ord("a")] +=1
            l +=1

            if charCount1 == charCount2:
                return True
        
        return False






        
            


        