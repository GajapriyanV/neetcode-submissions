class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dp = [[0] * COLS for _ in range(ROWS)]

        curColSum = 0
        for i in range(ROWS - 1, -1, -1):
            curColSum += grid[i][COLS - 1]
            dp[i][COLS - 1] = curColSum

        curRowSum = 0
        for j in range(COLS - 1, -1, -1):
            curRowSum += grid[ROWS - 1][j]
            dp[ROWS - 1][j] = curRowSum

        for i in range(ROWS - 2, -1, -1):
            for j in range(COLS - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

        return dp[0][0]