class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        

        cur = 0
        res = 0
        for i in range(len(gas)):

            if cur < 0:
                res = i
                cur = 0

            cur += gas[i]
            cur -= cost[i]
        
        return res



        