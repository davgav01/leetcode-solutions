"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        exponents = {"e", "E"}
        signs = {"+", "-"}

        seen_digit = False
        used_decimal = False
        used_exponent = False

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in signs:
                # sign is only valid at start or right after exponent
                if i > 0 and s[i - 1] not in exponents:
                    return False

            elif ch == ".":
                # decimal not allowed after exponent or if already used
                if used_decimal or used_exponent:
                    return False
                used_decimal = True

            elif ch in exponents:
                # exponent must follow a digit and only appear once
                if used_exponent or not seen_digit:
                    return False
                used_exponent = True
                seen_digit = False  # must see digit after exponent

            else:
                return False

        return seen_digit


print(Solution().isNumber("+."))
