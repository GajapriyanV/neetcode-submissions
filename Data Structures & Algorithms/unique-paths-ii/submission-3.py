class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for _ in range(ROWS)]


        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        

        for c in range(COLS - 1, -1, -1):
            if obstacleGrid[ROWS - 1][c] == 0:
                dp[ROWS - 1][c] = 1
            else:
                break
        
        for r in range(ROWS - 1, -1, -1):
            if obstacleGrid[r][COLS - 1] == 0:
                dp[r][COLS - 1] = 1
            else:
                break
        

        for i in range(ROWS - 2, -1, -1):
            for j in range(COLS - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j -1])
        
        return dp[0][0]