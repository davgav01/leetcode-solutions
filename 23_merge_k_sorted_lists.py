"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional


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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]

        current_merged = self.mergeTwoLists(lists[0], lists[1])
        if k > 2:
            for i in range(2, k):
                current_merged = self.mergeTwoLists(current_merged, lists[i])

        return current_merged
