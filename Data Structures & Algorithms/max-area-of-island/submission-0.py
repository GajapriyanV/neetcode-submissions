class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0"):
                return 0
            
            grid[r][c] = "0"

            res = 1

            res += dfs(r - 1, c)
            res += dfs(r + 1, c)
            res += dfs(r, c + 1)
            res += dfs(r, c - 1)

            return res

        
        maxIsland = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    maxIsland = max(maxIsland, dfs(i, j))
                 
        return maxIsland


        

        

        
        