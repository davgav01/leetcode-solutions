"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        count = 1
        for layer in range((n + 1) // 2):

            top_row = layer
            bottom_row = n - layer - 1
            left_column = layer
            right_column = n - layer - 1

            for i in range(left_column, right_column + 1):
                matrix[top_row][i] = count
                count += 1
            for i in range(top_row + 1, bottom_row + 1):
                matrix[i][right_column] = count
                count += 1

            if bottom_row == top_row:
                continue
            for i in range(right_column - 1, left_column - 1, -1):
                matrix[bottom_row][i] = count
                count += 1

            if left_column == right_column:
                continue
            for i in range(bottom_row - 1, top_row, -1):
                matrix[i][left_column] = count
                count += 1

        return matrix


print(Solution().generateMatrix(3))
