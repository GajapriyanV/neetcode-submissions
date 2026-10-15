class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1
        
        q = deque(["0000"])
        visit = set()
        visit.add("0000")

        steps = 0
        while q:
            for _ in range(len(q)):

                combination = q.popleft()

                if combination == target:
                    return steps
                
                for i in range(4):
                    curDigit = int(combination[i])
                    
                    for j in [1, -1]:
                        newDigit = (curDigit + j) % 10
                        newCombination = combination[:i] + str(newDigit) + combination[i + 1:]
                        if newCombination not in visit and newCombination not in deadends:
                            q.append(newCombination)
                            visit.add(newCombination)
            
            steps +=1
        
        return -1
                    
                    



        
