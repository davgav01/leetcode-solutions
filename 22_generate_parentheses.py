"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n):
        prev_strings = ["("]

        for i in range(2 * n - 1):
            strings = []
            for partial in prev_strings:
                close = sum([1 for para in partial if para == ")"])
                open = 1 + i - close
                if open > close:
                    strings.append(partial + ")")
                if open < n:
                    strings.append(partial + "(")
            prev_strings = strings

        return prev_strings


print(Solution().generateParenthesis(3))
