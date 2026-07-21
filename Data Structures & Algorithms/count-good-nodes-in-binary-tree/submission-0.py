# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0


        def dfs(node, pathMax):

            if not node:
                return 0
            
            nodeVal = 0 if pathMax > node.val else 1

            res = nodeVal
            res += dfs(node.left, max(pathMax, node.val))
            res += dfs(node.right, max(pathMax, node.val))

            return res
        
        return dfs(root, float("-infinity"))
        