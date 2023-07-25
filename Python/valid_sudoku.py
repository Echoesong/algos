# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Planning:
# I'll need to check three things:
#   1. All rows have only numbers 1-9 or else .
#   2. All columns have only numbers 1-9 or else .
#   3. All boxes have only numbers 1-9 or else .

# Brute force method:
# 1. Iterate over every row and make sure they use only #1-9 (once) or .
# If all rows pass, then

# 2. create 'column arrays' to be iterated over, then:
# Iterate over every column and make sure they use only #1-9 (once) or .
# If all columns pass, then

# 3. create 'box arrays' to be iterated over, then:
# Iterate over every box and make sure they use only #1-9 (once) or .

# If all three groups of arrays return 0 for everything, the sudoku is valid.

# What data structures to use?
# Hash map, each row, column, and box will be able to pull from the value array and remove a number 1-9; if it can't pull, board is invalid.
#


def is_valid_sudoku(board):
    for row in board:
        for spot in row:
            nums_used = {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
            }
            num = row.pop()

    pass


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

is_valid_sudoku(board)
