"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        number_colours = len(nums)
        index_zero = 0
        index_two = number_colours - 1
        current_index = 0

        while current_index <= index_two:
            if nums[current_index] == 0:
                nums[index_zero], nums[current_index] = 0, nums[index_zero]
                index_zero += 1
                current_index += 1
            elif nums[current_index] == 2:
                nums[index_two], nums[current_index] = 2, nums[index_two]
                index_two -= 1
            else:
                current_index += 1

        print(nums)


Solution().sortColors([2, 0, 1])
