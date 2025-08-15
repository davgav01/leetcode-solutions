"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find any occurence of target
        left = 0
        right = len(nums) - 1
        any_index = -1
        while left <= right and any_index == -1:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                any_index = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if any_index == -1:
            return [-1, -1]

        max_left = left
        max_right = right
        left_index = any_index
        right = any_index
        while left <= right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if target == nums[mid] and nums[mid - 1] != target:
                left_index = mid
                break
            elif target == nums[left]:
                left_index = left
                break
            elif target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        right_index = any_index
        right = max_right
        left = any_index
        print("right search")
        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right)
            if target == nums[mid] and nums[mid + 1] != target:
                right_index = mid
                break
            elif target == nums[right]:
                right_index = right
                break
            elif target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return [left_index, right_index]


# print(Solution().searchRange([1, 2, 3, 4, 5, 5, 6, 7, 8], 5))
# print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([1], 1))
