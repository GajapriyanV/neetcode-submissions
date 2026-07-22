class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS, COLS = len(board), len(board[0])

        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        squareCheck = defaultdict(set)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowCheck[r] or board[r][c] in colCheck[c] or board[r][c] in squareCheck[(r // 3, c // 3)]):
                    return False
                

                rowCheck[r].add(board[r][c])
                colCheck[c].add(board[r][c])
                squareCheck[(r // 3, c // 3)].add(board[r][c])
        
        print(rowCheck)
        print(colCheck)
        print(squareCheck)
        return True



        