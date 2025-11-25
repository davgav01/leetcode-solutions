"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since s has only one 'a', we cannot find a valid window.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s), len(t)
        if tlen > slen:
            return ""

        need = Counter(t)
        left = 0
        best_len = float("inf")
        best_l = 0
        best_r = 0

        for right in range(slen):
            c = s[right]
            if c in need:
                need[c] -= 1

            # Shrink from the left while the window is still valid or has junk
            while left <= right and ((s[left] not in need) or (need[s[left]] < 0)):
                if s[left] in need:
                    need[s[left]] += 1
                left += 1

            # Check if window covers t
            if all(v <= 0 for v in need.values()):
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l, best_r = left, right

        if best_len == float("inf"):
            return ""
        return s[best_l : best_r + 1]


print(Solution().minWindow("abcd", "ad"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
