"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s

        result = []
        cycle_len = 2 * numRows - 2

        for row in range(numRows):
            for i in range(row, len(s), cycle_len):
                # Add character from current cycle
                result.append(s[i])

                # For middle rows, add the diagonal character if it exists
                if row != 0 and row != numRows - 1:
                    diagonal_idx = i + cycle_len - 2 * row
                    if diagonal_idx < len(s):
                        result.append(s[diagonal_idx])

        return "".join(result)


# Original implementation for comparison
class OriginalSolution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        numDiag = numRows - 2
        array = []
        while len(s) >= numRows + numDiag:
            array.append(s[:numRows])
            array.append(s[numRows - 1 : numRows + numDiag + 1][::-1])
            s = s[numRows + numDiag :]

        if len(s) > numRows:
            array.append(s[:numRows])
            array.append(s[numRows - 1 :][::-1])
        elif len(s) > 0:
            array.append(s)

        print(array)
        output = ""
        output += "".join([row[0] for row in array[::2]])
        for i in range(1, numRows - 1):
            output += "".join([row[i] for row in array if len(row) > i])
        output += "".join([row[-1] for row in array[::2] if len(row) == numRows])

        return output


# Test both implementations
if __name__ == "__main__":
    test_cases = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 1), ("AB", 1)]

    solution = Solution()
    original = OriginalSolution()

    for s, numRows in test_cases:
        optimized_result = solution.convert(s, numRows)
        print(f"Optimized: '{s}' with {numRows} rows -> '{optimized_result}'")

    print("\nOriginal implementation:")
    print(original.convert("PAYPALISHIRING", 4))
