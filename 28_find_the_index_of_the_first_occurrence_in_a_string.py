"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        first = needle[0]
        i = 0
        while i <= hlen - nlen:
            if haystack[i] == first and haystack[i : i + nlen] == needle:
                return i
            i += 1
        return -1


print(Solution().strStr("a", "a"))
