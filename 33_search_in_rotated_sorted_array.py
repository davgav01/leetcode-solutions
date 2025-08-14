"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def index_search(left_index: int, right_index: int) -> int:
            # Base case: 3 or fewer elements left
            if right_index - left_index <= 2:
                for idx in range(left_index, right_index + 1):
                    if nums[idx] == target:
                        return idx
                return -1

            mid_index = (left_index + right_index) // 2
            left_val, mid_val, right_val = (
                nums[left_index],
                nums[mid_index],
                nums[right_index],
            )

            if mid_val == target:
                return mid_index

            # Determine which half is sorted
            if left_val <= mid_val:
                # Left half is sorted
                if left_val <= target < mid_val:
                    return index_search(left_index, mid_index - 1)
                else:
                    return index_search(mid_index + 1, right_index)
            else:
                # Right half is sorted
                if mid_val < target <= right_val:
                    return index_search(mid_index + 1, right_index)
                else:
                    return index_search(left_index, mid_index - 1)

        return index_search(0, len(nums) - 1)


print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 1))
