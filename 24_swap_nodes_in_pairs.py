"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        while head and head.next:
            first = head
            second = head.next
            third = head.next.next

            prev.next = second
            prev.next.next = first
            prev.next.next.next = third
            prev = prev.next.next

            head = third

        return dummy.next


def list_to_linkedlist(lst):
    """Convert a Python list to a linked list and return the head."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


res = Solution().swapPairs(list_to_linkedlist([1, 2, 3, 4, 5]))
print(linkedlist_to_list(res))
