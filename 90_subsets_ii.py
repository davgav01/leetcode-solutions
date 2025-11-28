"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        outputs = [[]]
        seen = defaultdict(int)

        for number in nums:
            if number not in seen:
                outputs += [output + [number] for output in outputs]
            else:
                outputs += [
                    output + [number]
                    for output in outputs
                    if Counter(output)[number] == seen[number]
                ]

            seen[number] += 1

        return outputs


# First solution was correct but larger constants in big-O time
# Here is the canonical solution:
from typing import List


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = [[]]
        start = 0

        for i, num in enumerate(nums):
            # If it's a duplicate, only extend subsets created in the previous step
            if i > 0 and nums[i] == nums[i - 1]:
                new_start = prev_size
            else:
                new_start = 0

            prev_size = len(res)
            for j in range(new_start, prev_size):
                res.append(res[j] + [num])

        return res
