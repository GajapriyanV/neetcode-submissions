class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.res = root.val
        self.i = k

        def dfs(root):
            if not root or self.i == 0:
                return

            dfs(root.left)

            if self.i == 0:
                return

            self.i -= 1
            if self.i == 0:
                self.res = root.val
                return

            dfs(root.right)

        dfs(root)
        return self.res