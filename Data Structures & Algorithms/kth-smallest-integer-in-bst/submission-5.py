
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        self.k = k

        def dfs(root):
            nonlocal res

            if not root or self.k == 0:
                return

            dfs(root.left)

            if self.k == 0:
                return

            self.k -= 1
            if self.k == 0:
                res = root.val
                return

            dfs(root.right)

        dfs(root)
        return res
