"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        perms = []
        ln = len(nums)

        def backtrack(start):
            if start == ln - 1:
                perms.append(nums.copy())
            else:
                swapped = set()
                for i in range(start, ln):
                    if nums[i] in swapped:
                        continue
                    swapped.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return perms


print(Solution().permuteUnique([2, 1, 1, 2]))
