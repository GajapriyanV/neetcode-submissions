class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0

        q = deque([])
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh +=1
        
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if new_x >= 0 and new_x < ROWS and new_y >= 0 and new_y < COLS and grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        fresh -=1

            
            res +=1
        
        return res if fresh == 0 else -1


                


                

        