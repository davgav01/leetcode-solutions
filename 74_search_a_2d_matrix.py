"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows, ncols = len(matrix), len(matrix[0])
        first_col = [row[0] for row in matrix]

        if target in first_col:
            return True

        left, right = 0, nrows - 1
        while (right - left) > 1:
            mid = (left + right) // 2
            if first_col[mid] > target:
                right = mid
            else:
                left = mid

        if target > first_col[right]:
            possible_col = matrix[right]
        else:
            possible_col = matrix[left]

        left, right = 0, ncols - 1
        while right - left > 1:
            mid = (left + right) // 2
            if (possible_col[right] == target) or (possible_col[left] == target):
                return True
            elif possible_col[mid] > target:
                right = mid
            else:
                left = mid

        if (possible_col[right] == target) or (possible_col[left] == target):
            return True
        return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(
    Solution().searchMatrix(
        [
            [-9, -7, -7, -5, -3],
            [-1, 0, 1, 3, 3],
            [5, 7, 9, 11, 12],
            [13, 14, 15, 16, 18],
            [19, 21, 22, 22, 22],
        ],
        -4,
    )
)
