"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        spiral = []
        for layer in range((min(n, m) + 1) // 2):
            top_row = layer
            bottom_row = n - layer - 1
            left_column = layer
            right_column = m - layer - 1

            for i in range(left_column, right_column + 1):
                spiral.append(matrix[top_row][i])
            for i in range(top_row + 1, bottom_row + 1):
                spiral.append(matrix[i][right_column])

            if bottom_row == top_row:
                continue
            for i in range(right_column - 1, left_column - 1, -1):
                spiral.append(matrix[bottom_row][i])

            if left_column == right_column:
                continue
            for i in range(bottom_row - 1, top_row, -1):
                spiral.append(matrix[i][left_column])

        return spiral


mat1 = [[1], [5], [9]]
print(Solution().spiralOrder(mat1))
