# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True

        def dfs(root):
            nonlocal isBalanced

            if not root:
                return 0
            
            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)

            if abs(leftSubTree - rightSubTree) > 1:
                isBalanced = False
            
            return 1 + max(leftSubTree, rightSubTree)
        
        dfs(root)

        return isBalanced
        