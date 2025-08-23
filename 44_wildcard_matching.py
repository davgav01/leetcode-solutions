"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false

Constraints:
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)

        @lru_cache(None)
        def dp(i, j):
            if j == lp:
                return i == ls
            if i == ls:
                # Remaining pattern must be all '*'
                return all(x == "*" for x in p[j:])

            if p[j] == s[i] or p[j] == "?":
                return dp(i + 1, j + 1)
            elif p[j] == "*":
                # '*' can match empty or one+ characters
                return dp(i, j + 1) or dp(i + 1, j)
            else:
                return False

        return dp(0, 0)


print(Solution().isMatch("mississippi", "m??*ss*?i*pi"))
