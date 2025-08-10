"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        l_pref = len(prefix)
        if len(strs) == 1:
            return prefix

        i = 1
        while i < len(strs) and l_pref > 0:
            s = strs[i]
            l_pref = min(len(s), l_pref)
            while l_pref > 0 and s[:l_pref] != prefix[:l_pref]:
                l_pref -= 1
                print(l_pref)
            i += 1
        return prefix[:l_pref]


print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
