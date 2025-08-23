"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        steps_remaining = nums[0]
        if len(nums) == 1:
            return 0

        current_max = 0
        n_jumps = 1
        i = 0
        while i + steps_remaining < len(nums) - 1:
            i += 1
            steps_remaining -= 1
            if nums[i] - steps_remaining > current_max:
                current_max = nums[i] - steps_remaining

            if steps_remaining == 0:
                steps_remaining = current_max
                current_max = 0
                n_jumps += 1

        return n_jumps


jumps = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]

print(Solution().jump(jumps))
# print(Solution().jump([2, 3, 0, 1, 4]))
