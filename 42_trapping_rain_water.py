"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


# Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# Solution().trap([4, 2, 0, 3, 2, 5])
heights1 = [
    1000,
    999,
    998,
    997,
    996,
    995,
    994,
    993,
    992,
    991,
    990,
    989,
    988,
    987,
    986,
    985,
    984,
    983,
    982,
    981,
    980,
    979,
    978,
    977,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
    966,
]
Solution().trap(heights1)
