# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, prevMax):
            if not node:
                return 0
            
            curNodeCount = 0

            if node.val > prevMax:
                curNodeCount +=1
            
            newMax = max(node.val, prevMax)

            left = dfs(node.left, newMax)
            right = dfs(node.right, newMax)

            return curNodeCount + left + right
        
        return dfs(root, float("-inf"))
        