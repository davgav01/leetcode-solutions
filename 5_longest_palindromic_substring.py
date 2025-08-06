"""
Given a string s, return the longest in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""


class Solution(object):
    def is_palindrome(self, cs):
        return cs[: (len(cs)) // 2] == cs[(len(cs) + 1) // 2 :][::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[0]
        llen = 0
        offset = 0
        letter_hash = {}
        letter_set = set(s)
        for letter in letter_set:
            letter_hash[letter] = [i for i, char in enumerate(s) if char == letter]
        while len(s) > llen:
            current_letter = s[0]
            letter_index_valid = [
                i - offset for i in letter_hash[current_letter] if i - offset >= llen
            ]
            for index in letter_index_valid[::-1]:
                if index < llen:
                    continue
                if self.is_palindrome(s[: index + 1]):
                    longest = s[: index + 1]
                    llen = len(longest)

            s = s[1:]
            offset += 1
        return longest


print(Solution().longestPalindrome("aba"))
