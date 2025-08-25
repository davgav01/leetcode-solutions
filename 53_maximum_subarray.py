"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_nums = max(nums)
        if max_nums <= 0:
            return max_nums

        index = 0
        max_run = 0
        current_run = 0
        while index < len(nums):
            if nums[index] < 0:
                negs = 0
                while index < len(nums) and nums[index] < 0:
                    negs += nums[index]
                    index += 1

                if current_run > max_run:
                    max_run = current_run

                if current_run + negs <= 0:
                    current_run = 0
                else:
                    current_run += negs
            else:
                current_run += nums[index]
                index += 1

        return max([max_run, current_run])


print(Solution().maxSubArray([5, 4, -1, 7, 8]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
