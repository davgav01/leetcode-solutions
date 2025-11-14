"""
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation:
We say that "rgeat" is a scrambled string of "great".
One possible scenario represented in a tree:
    great
   /    \
  gr    eat
 / \    /  \
 g   r  e   at
           / \
          a   t
To scramble the string "great", we may choose the random index 2 and divide it into two substrings "gr" and "eat".
We decide to swap the two substrings, so we get "eatgr".
Then, we continue scrambling "eat" and "gr" separately.
For "eat", we may choose index 1 and get "e" and "at". We decide to keep the order, so we get "eat".
For "gr", we may choose index 1 and get "g" and "r". We decide to swap the order, so we get "rg".
Finally, we join "rg" and "eat" to get "rgeat", which is the same as s2.

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:
Input: s1 = "a", s2 = "a"
Output: true

Constraints:
s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.
"""
from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        pass
