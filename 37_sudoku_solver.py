"""
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A Sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the nine 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example:
Input: board = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["3","4","5","2","8","6","1","7","9"]]

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

from collections import defaultdict
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_digits = []
        column_digits = []
        for i, row in enumerate(board):
            row_digits.append(set([j for j in row if j != "."]))
            column_digits.append(
                set([board[r][i] for r in range(9) if board[r][i] != "."])
            )

        square_digits = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_digits.append(
                    set(
                        [
                            board[x][y]
                            for x in range(i, i + 3)
                            for y in range(j, j + 3)
                            if board[x][y] != "."
                        ]
                    )
                )

        def get_square(i, j):
            return (j // 3) + 3 * (i // 3)

        unfilled_indexes = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    unfilled_indexes.add((i, j))

        full_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        while len(unfilled_indexes):
            filled = set()
            for i, j in unfilled_indexes:
                seen = row_digits[i].union(
                    column_digits[j].union(square_digits[get_square(i, j)])
                )
                needed = full_set - seen

                if len(needed) == 1:
                    fill_number = needed.pop()
                    board[i][j] = fill_number
                    filled.add((i, j))
                    row_digits[i].add(fill_number)
                    column_digits[j].add(fill_number)
                    square_digits[get_square(i, j)].add(fill_number)
                    # print("position_filled ", i, j, unfilled_indexes)
                # print(i, j, seen, needed, full_set)
            unfilled_indexes = unfilled_indexes - filled

        for row in board:
            print(row)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Track used numbers in rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def get_box(i, j):
            return (i // 3) * 3 + (j // 3)

        # Initialize sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[get_box(i, j)].add(val)

        digits = {str(x) for x in range(1, 10)}

        # Constraint propagation: fill forced cells
        def fill_forced():
            progress = True
            while progress:
                progress = False
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            box = get_box(i, j)
                            candidates = digits - rows[i] - cols[j] - boxes[box]
                            if len(candidates) == 1:
                                num = candidates.pop()
                                board[i][j] = num
                                rows[i].add(num)
                                cols[j].add(num)
                                boxes[box].add(num)
                                progress = True

        fill_forced()

        # Backtracking, filling cells with fewest options first
        def backtrack():
            # Find the empty cell with the fewest candidates
            min_candidates = 10
            best_cell = None
            candidates = None

            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        box = get_box(i, j)
                        possible = digits - rows[i] - cols[j] - boxes[box]
                        if len(possible) < min_candidates:
                            min_candidates = len(possible)
                            best_cell = (i, j)
                            candidates = possible
                        if min_candidates == 1:  # can't do better
                            break
                if min_candidates == 1:
                    break

            # If no empty cells, puzzle is solved
            if not best_cell:
                return True

            i, j = best_cell
            box = get_box(i, j)

            for num in candidates:
                # Place number
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

                if backtrack():
                    return True

                # Undo
                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[box].remove(num)

            return False

        backtrack()

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

Solution().solveSudoku(board1)
