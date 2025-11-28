"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows, ncols = len(board), len(board[0])
        nletters = len(word)

        def search(row, col, word_index):
            if word_index == nletters:
                return True
            letter = word[word_index]

            if row > 0 and [row - 1, col] not in used and board[row - 1][col] == letter:
                used.append([row - 1, col])
                if search(row - 1, col, word_index + 1):
                    return True
                used.pop()

            if (
                row < nrows - 1
                and [row + 1, col] not in used
                and board[row + 1][col] == letter
            ):
                used.append([row + 1, col])
                if search(row + 1, col, word_index + 1):
                    return True
                used.pop()

            if col > 0 and [row, col - 1] not in used and board[row][col - 1] == letter:
                used.append([row, col - 1])
                if search(row, col - 1, word_index + 1):
                    return True
                used.pop()

            if (
                col < ncols - 1
                and [row, col + 1] not in used
                and board[row][col + 1] == letter
            ):
                used.append([row, col + 1])
                if search(row, col + 1, word_index + 1):
                    return True
                used.pop()

            return False

        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == word[0]:
                    used = [[row, col]]
                    if search(row, col, 1):
                        return True

        return False


print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)
