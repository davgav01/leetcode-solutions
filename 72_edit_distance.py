"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Substitute a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
execution -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

from functools import lru_cache


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        lenWord1, lenWord2 = len(word1), len(word2)

        @lru_cache()
        def dps(i, j):
            if i < 0:
                # would have to delete j letters for them to match
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                # letters match, go left one letter each with no operations needed
                return dps(i - 1, j - 1)
            else:
                # letters don't match, +1 for operation needed, three choices
                # i-1, j-1: substitute letter
                # i-1, j: delete from word1
                # i, j-1: delete from word2
                return 1 + min([dps(i - 1, j), dps(i, j - 1), dps(i - 1, j - 1)])

        return dps(lenWord1 - 1, lenWord2 - 1)


print(Solution().minDistance("abc", "adc"))
