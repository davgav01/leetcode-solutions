"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all permutations of the array are sorted in one container, then the next permutation is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

You must replace the array in-place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        i -= 1
        j = i
        if j >= 0:
            while j < len(nums) - 1 and nums[i] < nums[j + 1]:
                j += 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            nums[i + 1 :] = reversed(nums[i + 1 :])
        else:
            nums.reverse()

        return nums


print(Solution().nextPermutation([1, 2, 3, 4, 5]))
print(Solution().nextPermutation([1, 2, 3, 5, 5]))
print(Solution().nextPermutation([5, 4, 3, 2, 1]))
print(Solution().nextPermutation([1, 3, 2]))
