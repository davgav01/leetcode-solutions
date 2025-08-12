"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            dummy_node = ListNode(0, list2)
            list2 = list2.next if list2.next else None
        else:
            dummy_node = ListNode(0, list1)
            list1 = list1.next if list1.next else None
        dummy_next = dummy_node.next

        while list1 and list2:
            if list1.val > list2.val:
                dummy_next.next = list2
                dummy_next = dummy_next.next
                list2 = list2.next if list2.next else None
            else:
                dummy_next.next = list1
                dummy_next = dummy_next.next
                list1 = list1.next if list1.next else None

        if list2:
            dummy_next.next = list2
        elif list1:
            dummy_next.next = list1

        return dummy_node.next
