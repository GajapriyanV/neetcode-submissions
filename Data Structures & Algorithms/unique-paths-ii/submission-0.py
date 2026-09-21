class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[M - 1][N - 1] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] != 1:
                    dp[r][c] += dp[r + 1][c]
                    dp[r][c] += dp[r][c + 1]

        return dp[0][0]