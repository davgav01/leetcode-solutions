"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: list[int]):
        ln = len(nums)

        def get_perms(checked):
            perms = []

            for i in range(ln):
                if i in checked:
                    continue

                if len(checked) == ln - 1:
                    return [[nums[i]]]

                inner_perms = get_perms(checked.union({i}))

                for j in range(len(inner_perms)):
                    perms.append(inner_perms[j] + [nums[i]])

            return perms

        print(get_perms(set()))


Solution().permute([1, 2, 3])
