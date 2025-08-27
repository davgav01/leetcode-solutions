"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for k in range(1,n):
            grid[0][k] += grid[0][k-1]
        for l in range(1,m):
            grid[l][0] += grid[l-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        return grid[m-1][n-1]
