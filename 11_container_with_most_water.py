"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4

Solution notes:
    This one was easy, very quick to do and beat 97.7% of users on first go.
"""


class Solution:
    def area(self, height, i, j):
        return abs(i - j) * min(height[i], height[j])

    def maxArea(self, height):
        maxA = 0
        i = 0
        j = len(height) - 1
        if i == j:
            return 0
        maxA = self.area(height, i, j)
        heights = [height[i], height[j]]
        while j > i:
            if height[i] < height[j]:
                while j > i and height[i] <= heights[0]:
                    i += 1
                heights[0] = height[i]
            elif height[i] > height[j]:
                while j > i and height[j] <= heights[1]:
                    j -= 1
                heights[1] = height[j]
            else:
                i += 1
                j -= 1
                if height[i] > height[j]:
                    j += 1  # put it back to where it was
                elif height[i] < height[j]:
                    i -= 1

            maxA = max(maxA, self.area(height, i, j))

        return maxA


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
