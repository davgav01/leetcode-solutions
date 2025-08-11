"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10**4 <= target <= 10**4
"""


class Solution:
    def threeSumClosest(self, nums, target):
        lnums = len(nums)
        nums.sort()
        closest = sum(nums[:3])
        seen = set()
        for i in range(lnums - 2):
            num1 = nums[i]
            if num1 in seen:
                continue
            seen.add(num1)
            j = i + 1
            k = lnums - 1
            while k > j:
                current_sum = num1 + nums[j] + nums[k]
                if current_sum == target:
                    return target
                elif current_sum > target:
                    k -= 1
                else:
                    j += 1
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
        return closest


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
