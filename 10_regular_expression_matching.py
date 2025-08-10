"""
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def index_next_valid(self, string, next_valid):
        i = 0
        if next_valid == ".":
            return i

        while string[i] != next_valid:
            i += 1
        return i

    def next_special(self, string):
        i = 0
        if "." not in string and "*" not in string:
            return None, len(string)
        while string[i] not in ".*":
            i += 1
        current = string[i]
        if current == "." and i < len(string) - 1 and string[i + 1] == "*":
            return ".*", i
        return current, i

    def next_not_pchar(self, string, char):
        i = 0
        slen = len(string)
        while i < slen and string[i] == char:
            i += 1
        return i

    def next_valid_not_star(self, string):
        i = 0
        slen = len(string)
        string_alt = string + " "
        print("pre_loop", string_alt, i)
        while i < slen and (string_alt[i] == "*" or string_alt[i + 1] == "*"):
            print("string alt", string_alt, i, string_alt[i + 1])
            i += 1
        print("post loop", string_alt, i)
        if i >= slen:
            valid_char = None
        else:
            valid_char = string[i]
        return valid_char, i

    def reduce_p(self, p):
        new_p = ""
        p_temp = p + "  "
        i = 0
        current_star = ""
        while i < len(p):
            if p_temp[i + 1] != "*":
                new_p += p_temp[i]
                current_star = ""
                i += 1
                continue
            elif current_star == p_temp[i] or current_star == ".":
                i += 2
                continue
            elif p_temp[i] == "." and current_star != "":
                new_p = new_p[:-2]

            new_p += p_temp[i]
            new_p += p_temp[i + 1]
            current_star = p_temp[i]
            i += 2
        return new_p

    def isMatch(self, s, p):
        # print("isMatch call", s, p)
        if s == p:
            return True
        p = self.reduce_p(p)
        print("isMatch call", s, p)
        char, index = self.next_special(p)
        print(char, index)
        if char == None:
            return s == p
        elif char == ".":
            print(". case=================", s, p, index, s[index + 1 :])
            if index >= len(s):
                return False
            return s[:index] == p[:index] and self.isMatch(
                s[index + 1 :], p[index + 1 :]
            )
        elif char == "*":
            sindex = index - 1
            if index != 1 and s[:sindex] != p[: index - 1]:
                return False
            pchar = p[index - 1]

            while sindex < len(s) and s[sindex] == pchar:
                if self.isMatch(s[sindex:], p[index + 1 :]):
                    return True
                sindex += 1
            if sindex >= len(s):
                return self.isMatch("", p[index + 1 :])
            return self.isMatch(s[sindex:], p[index + 1 :])
        else:  # ".*"
            sindex = index
            if index != 0 and s[:sindex] != p[:index]:
                return False

            if index + 2 >= len(p):
                return True

            while sindex < len(s):
                if self.isMatch(s[sindex:], p[index + 2 :]):
                    return True
                sindex += 1
            if sindex >= len(s):
                return self.isMatch("", p[index + 1 :])
            return self.isMatch(s[sindex:], p[index + 1 :])


# print(Solution().isMatch("ab", ".*"))
print(Solution().isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))
# print(Solution().isMatch("mississippi", "mis*is*p*."))
