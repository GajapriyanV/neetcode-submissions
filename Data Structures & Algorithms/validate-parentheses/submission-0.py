class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                if stack and closeToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False

        