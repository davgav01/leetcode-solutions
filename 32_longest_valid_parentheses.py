"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 3 * 10^4
s[i] is '(' or ')'.
"""


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        left = right = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                best = max(best, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for ch in reversed(s):
            if ch == ")":
                right += 1
            else:
                left += 1
            if left == right:
                best = max(best, 2 * left)
            elif left > right:
                left = right = 0

        return best


from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        best = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # new base after an unmatched ')'
                else:
                    best = max(best, i - stack[-1])
        return best


print(Solution().longestValidParentheses("())()(("))
