class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordering = {w: i for i, w in enumerate(order)}


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            minLen = min(len(w1), len(w2))

            if len(w2) < len(w1) and w2[:minLen] == w1[:minLen]:
                return False
            
            for i in range(minLen):
                if ordering[w2[i]] < ordering[w1[i]]:
                    return False
            
        
        return True
        