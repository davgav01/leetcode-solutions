"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        sign_dividend = sign_divisor = 1
        if dividend < 0:
            sign_dividend = -1
            dividend = -dividend
        if divisor < 0:
            sign_divisor = -1
            divisor = -divisor
        output_sign = sign_dividend * sign_divisor

        max_count = 2**31
        while dividend >= divisor and count <= max_count:
            div_value = divisor
            div_count_value = 1
            while dividend >= div_value and count <= max_count:
                dividend -= div_value
                count += div_count_value
                div_value += div_value
                div_count_value += div_count_value
        if output_sign == -1:
            return max(-max_count, -count)

        return min(max_count - 1, count)


print(Solution().divide(100, 3))
