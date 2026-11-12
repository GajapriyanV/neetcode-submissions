# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        indexStore = {val: index for val, index in enumerate(inorder)}
        self.i = 0

        def dfs(l, r):

            if l > r:
                return None
            
            root = TreeNode(preorder[self.i])
            indexOfPre = indexStore[preorder[self.i]]
            self.i += 1

            root.left = dfs(l, indexOfPre - 1)
            root.right = dfs(indexOfPre + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)
            
