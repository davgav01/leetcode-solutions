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

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]

        dummy_node = ListNode()
        dummy_node_copy = dummy_node
        counter = 0
        heap = []
        for l in lists:
            if l:
                heap.append((l.val, counter, l))
            counter += 1
        heapq.heapify(heap)

        while heap:
            _, _, current_smallest_node = heapq.heappop(heap)
            dummy_node.next = current_smallest_node
            dummy_node = dummy_node.next

            current_smallest_node = (
                current_smallest_node.next if current_smallest_node.next else None
            )
            if current_smallest_node:
                heapq.heappush(
                    heap, (current_smallest_node.val, counter, current_smallest_node)
                )
                counter += 1

        return dummy_node_copy.next
