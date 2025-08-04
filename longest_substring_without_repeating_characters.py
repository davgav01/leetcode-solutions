"""
LeetCode Problem 3: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Description:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {} 
        max_length = 0
        current_length = 0
        index = 0

        while index < len(s):
            char = s[index]
            current_length += 1  
            if char in last_seen:
                index = last_seen[char]+1
                last_seen = {}
                max_length = max(max_length,current_length-1)
                current_length = 0
            else:
                last_seen[char] = index
                index += 1

        max_length = max(max_length,current_length)
        print(last_seen)
        return max_length

print(Solution().lengthOfLongestSubstring("aab"))