# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for indx, row in board:
            
          if len(row) != len(set(row)):
              return False
          if len(row) != len(set( [board[x[indx]] for x in range(len(row)) ])):
              return False
        return True  

print([i for i in ["","0","2"] if i != ""])