from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        cnt = 0

        radiant = senate.count("R")
        dire = senate.count("D")

        while radiant > 0 and dire > 0:
            c = q.popleft()

            if c == "R":
                if cnt >= 0:
                    q.append("R")
                else:
                    radiant -= 1
                cnt += 1

            else:
                if cnt <= 0:
                    q.append("D")
                else:
                    dire -= 1
                cnt -= 1

        return "Radiant" if radiant > 0 else "Dire"