"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration of s and t such that:
- s and t are split into zero or more substrings consecutively.
- The interleaving is the concatenation of these parts, where it alternates taking these strings' parts in turn.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aac", s2 = "db", s3 = "aacdbb"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass
