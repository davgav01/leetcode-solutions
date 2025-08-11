"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
"""


class Solution:
    def threeSum(self, nums):
        output = set()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    triplet = tuple(sorted((nums[i], nums[j], complement)))
                    output.add(triplet)
                seen.add(nums[j])

        return list(output)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
