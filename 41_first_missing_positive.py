"""
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            val = nums[i]
            if -1 < val - 1 < i:
                nums[val - 1] = val
                i += 1
            elif val - 1 > i and val - 1 < len(nums) and nums[val - 1] != val:
                nums[i], nums[val - 1] = nums[val - 1], val
            else:
                i += 1

        j = 0
        while j < len(nums) and j + 1 == nums[j]:
            j += 1
        return j + 1


Solution().firstMissingPositive([7, 8, 9, 10, 11, 12])
Solution().firstMissingPositive([1, 2, 0])
Solution().firstMissingPositive([0, 2, 2, 4, 0, 1, 0, 1, 3])
Solution().firstMissingPositive([2, 1])
