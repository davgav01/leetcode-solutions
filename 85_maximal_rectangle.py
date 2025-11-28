"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: Output: 6

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nrows, ncols = len(matrix), len(matrix[0])
        # if we convert each value to be the number of consecutive 1s
        # from above it until that value, then we can treat it as a height
        # and use the previous solution, applying to each row and using the
        # max from all runs as the answer
        for i in range(nrows):
            for j in range(ncols):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1 and i != 0:
                    matrix[i][j] = matrix[i - 1][j] + 1

        def largestRectangleArea(heights: List[int]) -> int:
            n_heights = len(heights)
            left, right = 0, 0
            max_area = 0

            for i, h in enumerate(heights):
                left, right = i, i
                while left > 0 and heights[left - 1] >= h:
                    left -= 1
                while right < n_heights - 1 and heights[right + 1] >= h:
                    right += 1

                current_area = (1 + right - left) * h
                max_area = max([max_area, current_area])

            return max_area

        max_area = 0
        for row in matrix:
            row_max = largestRectangleArea(row)
            max_area = max([max_area, row_max])

        return max_area


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
