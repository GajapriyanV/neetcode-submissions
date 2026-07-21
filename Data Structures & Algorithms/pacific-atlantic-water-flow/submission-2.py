class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pacificVisit = set()
        atlanticVisit = set()
        res = []

        def dfs(r, c, prevVal, visit):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or heights[r][c] <= prevVal):
                return
            
            visit.add((r, c))

            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
        

        for c in range(COLS):

            dfs(0, c, -1, pacificVisit)

            dfs(ROWS - 1, c, -1, atlanticVisit)
        
        for r in range(ROWS):

            dfs(r, 0, -1, pacificVisit)

            dfs(r, COLS - 1, -1, atlanticVisit)
        

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificVisit and (r, c) in atlanticVisit:
                    res.append([r,c])
        
        return res
        


