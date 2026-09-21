class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(i ,j):

            if (i, j) in visit:
                return 0
            
            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return 1
            
            curPerim = 0
            visit.add((i, j))

            curPerim += dfs(i + 1, j)
            curPerim += dfs(i - 1, j)
            curPerim += dfs(i, j + 1)
            curPerim += dfs(i, j - 1)

            return curPerim


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i, j)



        