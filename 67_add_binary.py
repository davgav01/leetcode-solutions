"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            num_a = ord(a[i]) - ord("0") if i >= 0 else 0
            num_b = ord(b[j]) - ord("0") if j >= 0 else 0
            summed = carry + num_a + num_b
            result.append((summed) % 2)
            carry = (summed) // 2
            i -= 1
            j -= 1
        if carry:
            result.append(carry)
        return "".join(map(str, reversed(result)))


print(Solution().addBinary("1010", "1011"))
