from collections import defaultdict

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
def validSudoku(board):
    row=defaultdict(set)
    col=defaultdict(set)
    box=defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==".":
                continue
            if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(i//3,j//3)]:
                return False
            else:
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3,j//3)].add(board[i][j])
    return True

print(validSudoku(board))