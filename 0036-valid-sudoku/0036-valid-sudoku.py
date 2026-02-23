class Solution(object):
    def isValidSudoku(self, board):
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        squ=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if(board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in squ[(i//3,j//3)]):
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                squ[i//3,j//3].add(board[i][j])
        return True

        
        