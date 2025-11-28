"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false otherwise.

You must solve this problem as efficiently as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        if right == left:
            return nums[left] == target

        while left < right:
            mid = (right + left) // 2
            print(left, mid, right)
            if target in [nums[left], nums[mid], nums[right]]:
                return True

            if nums[left] == nums[right]:
                left += 1
                right -= 1
                continue

            if nums[mid] <= nums[right]:
                # pivot is between mid and left, right side is sorted
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # pivot is between mid and right. Left side is sorted
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False


# print(Solution().search([2, 5, 6, 6, 6, 7, 0, 0, 1, 2], 0))
print(Solution().search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2))
