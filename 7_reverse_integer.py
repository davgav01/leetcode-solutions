"""
Given a signed 32-bit integer x, return x with its ds reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21



Constraints:

    -2^31 <= x <= 2^31 - 1

Solution Notes:
    This was successful on the first attempt and beat 93% of users.
"""


class Solution(object):
    def __init__(self):
        self.len31 = len(str(2**31))

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            return -1 * self.reverse_positive(-1 * x)

        return self.reverse_positive(x)

    def reverse_positive(self, x):

        nlen = len(str(x))

        if nlen == 1:
            return x
        elif nlen < self.len31:
            output = (10 ** (nlen - 1)) * (x % 10)
            output += self.reverse_positive(x // 10)
            return output
        else:
            # We will deal with the case of len31==nlen by breaking it up
            # into first digit and the last nlen-1 digits
            nm1 = x % (10 ** (nlen - 1))
            first = x // (10 ** (nlen - 1))
            reverse_nm1 = self.reverse_positive(nm1)

            limit = 2**31 - 1
            limitf = limit // 10
            limitl = limit % 10

            if reverse_nm1 > limitf:
                return 0
            elif reverse_nm1 == limitf and first > limitl:
                return 0

            return 10 * reverse_nm1 + first


print(2**31)
print(Solution().reverse(123))
print(Solution().reverse(40))
print(Solution().reverse(5))
print(Solution().reverse(-23))
print(Solution().reverse(225))
print(Solution().reverse(-231))
print(Solution().reverse(1534236469))
