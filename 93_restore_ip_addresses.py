"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros except for the number 0 itself.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312", and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
1 <= s.length <= 20
s consists of digits only.
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ips = []
        digits = len(s)

        def dfs(index, dots, path):

            if dots > 3 or index >= digits:
                return

            next_3 = s[index : index + 3]
            if (
                dots == 3
                and int(next_3) < 256
                and (next_3[0] != "0" or next_3 == "0")
                and index + 3 >= digits
            ):
                valid_ips.append(path + next_3)

            for i in range(1, len(next_3) + 1):
                possible_number = s[index : index + i]
                if (possible_number[0] != "0" or possible_number == "0") and int(
                    possible_number
                ) < 256:
                    dfs(index + i, dots + 1, path + s[index : index + i] + ".")

        dfs(0, 0, "")

        return valid_ips


print(Solution().restoreIpAddresses("25525511135"))
