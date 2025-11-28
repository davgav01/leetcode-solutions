"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

from typing import List


# This solution works but is too slow, brute force.
class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
            print(i, h, max_area, left, right)

        return max_area


# faster solution using stack method
# it keeps a stack of indices with increasing height.
# when the next element is smaller that the previous we go back through the stack
# and calculate possible areas.
# anything that is added to the stack after that is still increasing
# all smaller bigger values were popped and not needed anymore
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack: List[int] = []  # will store indices of bars in increasing height
        max_area = 0

        # Append a sentinel height 0 to flush out remaining bars
        for i in range(n + 1):
            # Current height: 0 after the end
            current_height = heights[i] if i < n else 0

            # If current bar is lower than the bar at stack top,
            # we can finalize areas for higher bars.
            while stack and current_height < heights[stack[-1]]:
                h_idx = stack.pop()
                h = heights[h_idx]

                # If stack empty, width is i (from 0 to i-1)
                # Else, width is between (stack[-1] + 1) and (i - 1)
                left_bound = stack[-1] if stack else -1
                width = i - left_bound - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
