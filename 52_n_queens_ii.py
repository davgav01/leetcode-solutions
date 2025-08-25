"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""

from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()  # row + col
        diag2 = set()  # row - col
        res = []
        solution = [["."] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in solution])
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                # place queen
                solution[row][col] = "Q"
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                dfs(row + 1)

                # backtrack
                solution[row][col] = "."
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        dfs(0)
        return len(res)
