class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            toAdd = True
            while stack and asteroid < 0 and stack[-1] > 0:

                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroid) < abs(stack[-1]):
                    toAdd = False
                    break
                else:
                    stack.pop()
                    toAdd = False
                    break
            
            if toAdd:
                stack.append(asteroid)
        
        return stack

                
                    


        