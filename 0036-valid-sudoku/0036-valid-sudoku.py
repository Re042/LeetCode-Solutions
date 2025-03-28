from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if (board[i][j] in rows[i] or board[i][j] in columns[j] 
                    or board[i][j] in squares[(i//3, j//3)]):
                        return False
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    squares[(i//3, j//3)].append(board[i][j])
        return True

