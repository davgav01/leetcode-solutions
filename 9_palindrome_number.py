"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2**31 <= x <= 2**31 - 1
"""


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        strx = str(x)
        l = len(strx)
        if l == 1:
            return True
        mid = l // 2
        for i in range(0, mid):
            j = l - i - 1
            if strx[i] != strx[j]:
                return False

        return True


class Solution:
    def isPalindrome(self, x):
        if 0 <= x < 10:
            return True
        if x < 0 or x % 10 == 0:
            return False

        reversed = 0
        num = x

        while num > reversed:
            reversed = reversed * 10 + num % 10
            num = num // 10

        output = (reversed == num) or (reversed == num // 10)
        return output


print(Solution().isPalindrome(123))
print(Solution().isPalindrome(-12321))
print(Solution().isPalindrome(435534))
