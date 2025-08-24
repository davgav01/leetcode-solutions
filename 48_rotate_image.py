"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotate the n x n matrix 90 degrees clockwise in place.
        """
        n = len(matrix)

        # Process the matrix layer by layer, from outermost to innermost
        for layer in range(n // 2):
            first = layer  # top row index of this layer
            last = n - 1 - layer  # bottom row index of this layer

            # Rotate the elements in this layer
            for i in range(first, last):
                offset = i - first

                # Save the top element
                top = matrix[first][i]

                # Move left -> top
                matrix[first][i] = matrix[last - offset][first]

                # Move bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]

                # Move right -> bottom
                matrix[last][last - offset] = matrix[i][last]

                # Move top -> right
                matrix[i][last] = top

        print(matrix)


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Solution().rotate(mat)
