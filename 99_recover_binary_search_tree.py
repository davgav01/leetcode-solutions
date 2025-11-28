"""
You are given the root of a binary search tree (BST), and exactly two of the nodes in the tree were swapped by mistake. Recover the BST.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1

Follow up: A solution using O(n) time and O(1) space would be very welcome.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify the tree in-place instead.
        """
        pass
