"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
"""


class Solution:
    def fourSum(self, nums, target):
        lnums = len(nums)
        nums.sort()
        results = set()

        def sorted3Sum(reduced_nums, remainder):
            output_set = set()
            seen = set()
            lreduced_nums = len(reduced_nums)
            for i in range(lreduced_nums - 2):
                num1 = reduced_nums[i]
                if num1 in seen:
                    continue
                seen.add(num1)

                j = i + 1
                k = lreduced_nums - 1
                while k > j:
                    current_sum = num1 + reduced_nums[j] + reduced_nums[k]
                    if current_sum == remainder:
                        triplet = tuple(
                            sorted([num1, reduced_nums[j], reduced_nums[k]])
                        )
                        output_set.add(triplet)
                        k -= 1
                        j += 1
                    elif current_sum > remainder:
                        k -= 1
                    else:
                        j += 1

            return output_set

        for i in range(lnums - 3):
            current = nums[i]
            remainder = target - current
            valid_set = sorted3Sum(nums[i + 1 :], remainder)
            valid_list = list(valid_set)
            for tup in valid_list:
                results.add(tuple(sorted([current] + list(tup))))

        return list(results)


print(Solution().fourSum([2, 2, 2, 2, 2], 8))
