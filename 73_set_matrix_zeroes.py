"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print(row)
        print("")

        ncols = len(matrix[0])
        nrows = len(matrix)
        current_row_zero = False
        prev_row_zero = False

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    # set all previous column entries to zero
                    k = i - 1
                    while k >= 0:
                        matrix[k][j] = 0
                        k -= 1
                    # when the time comes, this row will all be zeroes
                    current_row_zero = True

                # if the entry directly above in the column is zero, then this column is zero
                elif matrix[i - 1][j] == 0:
                    matrix[i][j] = 0

            # finish using prev row zeros to propagate zeroes down, can now set all to
            # zero if there was a zero in that row
            if prev_row_zero:
                matrix[i - 1] = [0] * ncols
            prev_row_zero, current_row_zero = current_row_zero, False

        # final check if there was a zero in the last row, set to zero
        if prev_row_zero:
            matrix[-1] = [0] * ncols

        for row in matrix:
            print(row)
        print("")


# Here is the canonical solution: use the first row as flags for setting each row/col to zero
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # 1. Determine if the first row or first col need to be zeroed
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 2. Use first row/col as flags for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. Zero out cells based on flags in the first row/col
        # Note: We skip the first row/col here to avoid overwriting flags prematurely
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. Handle the first row and first column separately using the booleans
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


mat1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
mat2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
mat3 = [
    [3, 5, 5, 6, 9, 1, 4, 5, 0, 5],
    [2, 7, 9, 5, 9, 5, 4, 9, 6, 8],
    [6, 0, 7, 8, 1, 0, 1, 6, 8, 1],
    [7, 2, 6, 5, 8, 5, 6, 5, 0, 6],
    [2, 3, 3, 1, 0, 4, 6, 5, 3, 5],
    [5, 9, 7, 3, 8, 8, 5, 1, 4, 3],
    [2, 4, 7, 9, 9, 8, 4, 7, 3, 7],
    [3, 5, 2, 8, 8, 2, 2, 4, 9, 8],
]
Solution().setZeroes(mat1)
Solution().setZeroes(mat2)
Solution().setZeroes(mat3)
