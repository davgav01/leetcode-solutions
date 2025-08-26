"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
ewInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals) and newInterval[0] >= intervals[i][0]:
            i += 1

        if i == 0:
            result = [newInterval]
            remainder = intervals
        else:
            result = intervals[:i]
            remainder = [newInterval] + intervals[i:]

        for i in range(0, len(remainder)):
            if remainder[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], remainder[i][1])
            else:
                result.append(remainder[i])

        return result


print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
print(Solution().insert([[1, 5]], [5, 7]))
print(Solution().insert([], [5, 7]))
