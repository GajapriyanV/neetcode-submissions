class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed))  # ascending position
        stack = []

        for p, s in pair:
            t = (target - p) / s

            while stack and stack[-1] <= t:
                stack.pop()

            stack.append(t)

        return len(stack)