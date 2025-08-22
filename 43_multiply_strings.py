"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integers directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= len(num1), len(num2) <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == 0 or num2 == 0:
            return "0"
        lnum1, lnum2 = len(num1), len(num2)
        output = (lnum1 + lnum2) * [0]
        ord0 = ord("0")

        for i in range(lnum1 - 1, -1, -1):
            for j in range(lnum2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord0
                digit2 = ord(num2[j]) - ord0
                temp = output[i + j + 1] + digit1 * digit2
                output[i + j + 1] = temp % 10
                output[i + j] += temp // 10

        result = "".join(map(str, output)) if output else "0"
        result = result if result else "0"
        print(result.lstrip("0"))


Solution().multiply("3", "2")
