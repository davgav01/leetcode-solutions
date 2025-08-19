"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains only one unique digit. Then, for each substring, say the number of digits, then say the digit. Finally, concatenate all the said digits.

For example, the saying and conversion for digit string "3322251":
"33" is two 3's, and "222" is three 2's, and "5" is one 5, and "1" is one 1.
This becomes "23" + "32" + "15" + "11".

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
1 <= n <= 30
"""


class Solution:
    def rle(self, string):
        if len(string) == 0:
            return ""
        i = 1
        while i < len(string) and string[i] == string[i - 1]:
            i += 1
        return str(i) + string[0] + self.rle(string[i:])

    def countAndSay(self, n: int) -> str:
        output = "1"

        for i in range(1, n):
            output = self.rle(output)
            print(output)

        print("final: ", n, " = ", output)
        return output


Solution().countAndSay(4)
