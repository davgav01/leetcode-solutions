"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 6 combinations of 2 numbers from 1 to 4 (the order of elements does not matter).

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 combination of 1 number from 1 to 1.

Constraints:
1 <= n <= 20
1 <= k <= n
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        outputs = [[1]]
        result = []

        for i in range(2, n + 1):
            # for each number, it starts, it extends from previous, or is skipped
            # it can only start if less than k from the end
            starts = [i]
            skipped = [combination.copy() for combination in outputs]

            extends = []
            for combination in outputs:
                combination.append(i)
                if len(combination) == k:
                    result.append(combination)
                else:
                    extends.append(combination)

            outputs = [starts]
            for partial_combination in extends:
                outputs.append(partial_combination)
            for partial_combination in skipped:
                outputs.append(partial_combination)

        return result


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            # If we've chosen k numbers, record the combination
            if len(path) == k:
                result.append(path.copy())
                return

            # Prune: we need (k - len(path)) more numbers,
            # so i can go at most to n - (k - len(path)) + 1
            max_start = n - (k - len(path)) + 1
            for i in range(start, max_start + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return result


print(Solution().combine(4, 2))
