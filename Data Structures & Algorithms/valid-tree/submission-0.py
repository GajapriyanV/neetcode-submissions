from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            toAdd = True
            while stack and stack[-1] > 0 and num < 0:
                if abs(stack[-1]) < abs(num):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(num):
                    toAdd = False
                    stack.pop()
                    break
                else:
                    toAdd = False
                    break
                
            if toAdd:
                stack.append(num)

        return stack