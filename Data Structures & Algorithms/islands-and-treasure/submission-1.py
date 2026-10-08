class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        steps = 0
        while q:
            steps +=1
            for _ in range(len(q)):
                r, c = q.popleft()

                for x, y in directions:
                    new_r, new_c = r + x, c + y

                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == (2^31) - 1:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = steps
        
        

        