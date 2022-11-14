# write a function to determine if a 9 x 9 Sudoku board, provided as
# an input parameter, is valid
# only the filled cells need to be validated according
# to the following rules:

# - each row must contain the digits 1-9 without repetition
# - each column must contain the digits 1-9 without repetition
# - each of the nine 3 x 3 sub-boxes of the board must contain
#   the digits 1-9 without repetition.

# note:
# - a Sudoku board (partially filled) could be valid
#   but is not necessarily solvable.
# - only the filled cells need to be validated
#   according to the mentioned rules

# example 1:

# input board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# output: True

# example 2:

# input board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# output: False

# explanation: same as example 1, except with the 5 in the
# top left corner being modified to 8; since there are
# two 8's in the top left 3x3 sub-box, the board is invalid

# constraints:
# - board.length == 9
# - board[i].length == 9
# - board[i][j] is a digit 1-9 or '.'
def checkRow(board: list[list]) -> bool:
    checkRow = []
    for i in range(9):
        for j in range(9):
            if board[i][j] in checkRow:
                return False
            elif board[i][j] == ".":
                continue
            else:
                checkRow.append(board[i][j])
                continue
        checkRow.clear()
    return True

def checkColumn(board: list[list]) -> bool:
    checkColumn = []
    for i in range(9):
        for j in range(9):
            if board[j][i] in checkColumn:
                return False
            elif board[j][i] == ".":
                continue
            else:
                checkColumn.append(board[j][i])
                continue
        checkColumn.clear()
    return True

def checkSquare(board: list[list]) -> bool:
    for row in range(0, 9, 3):
        for col in range(0,9,3):
            temp = []
            for r in range(row,row+3):
                for c in range(col, col+3):
                    if board[r][c] != 0:
                        temp.append(board[r][c])
            if len(temp) != len(set(temp)):
                return False
    return True 

def ValidSudoku(board : list[list]) -> bool:
    if checkRow(board) and checkColumn(board) and checkSquare(board):
        return True
    return False


if __name__ == "__main__":
    A = [["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]
    print(ValidSudoku(A))
    A = [["8","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]
    print(ValidSudoku(A))