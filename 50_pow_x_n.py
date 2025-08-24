"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            neg = True
            n = -n
        else:
            neg = False

        current_power = 1
        powers_of_x = [1, x]
        while 2 * current_power <= n:
            x = x * x
            powers_of_x.append(x)
            current_power *= 2

        res = 1
        index = len(powers_of_x) - 1
        while n > 0:
            if n < current_power:
                current_power //= 2
                index -= 1
            else:
                res *= powers_of_x[index]
                n -= current_power

        if neg:
            return 1 / res
        return res


print(Solution().myPow(3, -1))
