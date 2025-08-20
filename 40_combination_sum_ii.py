"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = Counter(candidates)
        candidates = sorted(set(candidates))
        res = set()
        path = []

        def dfs(start, remain):
            if remain == 0:
                path_tuple = tuple(path)
                if path_tuple not in res:
                    res.add(path_tuple)
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remain:
                    break
                path.append(val)
                if count[val]>1:
                    delta = 0
                    count[val] -= 1
                else:
                    delta = 1
                dfs(i+delta, remain - val)
                path.pop()
                if delta == 0:
                    count[val] += 1

        dfs(0, target)
        return list(res)

Solution().combinationSum([2, 3, 5, 6, 7, 8], 7)
