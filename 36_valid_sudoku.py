"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = [["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except the 5 in the top left corner is modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidList(l):
            count = Counter(l)
            for key, value in count.items():
                if key != "." and value > 1:
                    return False
            return True

        for row in board:
            if not isValidList(row):
                return False

        for column in zip(*board):
            if not isValidList(list(column)):
                return False

        subsquares = []
        threerows = [board[i : i + 3] for i in range(0, 9, 3)]
        for row1, row2, row3 in threerows:
            for j in range(0, 9, 3):
                square = []
                square.extend(row1[j : j + 3])
                square.extend(row2[j : j + 3])
                square.extend(row3[j : j + 3])
                subsquares.append(square)
        for square in subsquares:
            if not isValidList(square):
                return False
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidList(l):
            nums = [x for x in l if x != "."]
            return len(nums) == len(set(nums))

        # Check rows and columns
        for i in range(9):
            if not isValidList(board[i]) or not isValidList(
                [board[r][i] for r in range(9)]
            ):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not isValidList(square):
                    return False

        return True


board1 = [
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

print(Solution().isValidSudoku(board1))
