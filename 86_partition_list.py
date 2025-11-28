"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_node = ListNode(1)
        greater_than_node = ListNode(1)
        output_dummy_head = less_than_node
        greater_than_node_head = greater_than_node

        while head:
            if head.val < x:
                less_than_node.next = head
                less_than_node = less_than_node.next
            else:
                greater_than_node.next = head
                greater_than_node = greater_than_node.next
            head = head.next

        greater_than_node.next = None
        less_than_node.next = greater_than_node_head.next
        return output_dummy_head.next


# same solution but cleaner naming and with comments
class SolutionCleaner:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy heads for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        # Tails for building the two lists
        less = less_dummy
        greater = greater_dummy

        # Partition the list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        # Important: terminate the 'greater' list to avoid cycles
        greater.next = None

        # Link the two partitions: all < x followed by all >= x
        less.next = greater_dummy.next

        # The real head is the next of the less_dummy
        return less_dummy.next
