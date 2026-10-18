# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, maxC, minC):
            if not root:
                return True
            
            if not (minC < root.val < maxC):
                return False
            
            return dfs(root.left, root.val, minC) and dfs(root.right, maxC, root.val)
        
        return dfs(root, float("infinity"), float("-infinity"))

        
        