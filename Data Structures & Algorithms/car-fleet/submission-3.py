class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for i in range(len(pair)):
            t = (target - pair[i][0]) / pair[i][1]

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
        