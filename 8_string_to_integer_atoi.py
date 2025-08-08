"""
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-'
   or '+'. Read this character in if it is either. This determines if the
   final result is negative or positive respectively. Assume the result is
   positive if neither is present.
3. Read in next the characters until the next non-digit character or the end
   of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
   If no digits were read, then the integer is 0. Change the sign as
   necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
   then clamp the integer so that it remains in the range. Specifically,
   integers less than -231 should be clamped to -231, and integers greater
   than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

Note:
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest
  of the string after the digits.

Constraints:
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9),
  ' ', '+', '-', and '.'.

Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42

Example 3:
Input: s = "4193 with words"
Output: 4193
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        first_digit = len(s)
        end_of_numstring = first_digit
        if s == "":
            return 0

        for i, char in enumerate(s):
            is_digit = char in digits
            print(char in digits, char, digits)
            if is_digit and i < first_digit:
                first_digit = i
            elif not is_digit and i < first_digit:
                if char == " ":
                    continue
                if char in "-+" and (s + " ")[i + 1] in digits:
                    continue
                return 0
            elif not is_digit:
                end_of_numstring = i
                break

        if first_digit == len(s):
            return 0
        number = int(s[:end_of_numstring])
        print(number)
        if number > (2**31) - 1:
            number = (2**31) - 1
        elif number < -(2**31):
            return -(2**31)

        return number


print(Solution().myAtoi("422c0d322c0d3"))
print(Solution().myAtoi("   +042"))
