"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0, head)
        pivot = dummy.next
        end = pivot
        count = 1
        while end.next != None:
            end = end.next
            count += 1

        k = k % count
        if k == 0:
            return head

        while count > k + 1:
            pivot = pivot.next
            count -= 1
        end.next = dummy.next
        dummy.next = pivot.next
        pivot.next = None
        return dummy.next
