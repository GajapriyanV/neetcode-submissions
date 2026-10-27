# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(root, prevMax):

            if not root:
                return 0
            
            goodNode = 1 if root.val > prevMax else 0

            return goodNode + dfs(root.left, max(root.val, prevMax)), dfs(root.right, max(root.val, prevMax))
        
        return dfs(root, float("-inf"))
            


        