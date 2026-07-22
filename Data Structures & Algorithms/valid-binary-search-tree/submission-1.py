# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, minRoot, maxRoot):

            if not node:
                return True

            
            if not (minRoot < node.val < maxRoot):
                return False
            
            minSide = dfs(node.left, minRoot, node.val)
            maxSide = dfs(node.right, node.val, maxRoot)

            return minSide and maxSide
        
        return dfs(root, float("-infinity"), float("infinity"))
