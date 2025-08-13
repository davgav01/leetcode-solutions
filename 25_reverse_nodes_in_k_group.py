"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = dummy

        while head:
            n = 1
            temp_chain = head
            temp_chain_end = temp_chain
            head = head.next
            while n < k and head:
                temp_chain = ListNode(head.val, temp_chain)
                head = head.next
                n += 1
            if n < k:
                front.next = temp_chain_end
                break
            front.next = temp_chain
            temp_chain_end.next = head
            front = temp_chain_end

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


res = Solution().reverseKGroup(list_to_linkedlist([1, 2]), 2)
print(linkedlist_to_list(res))
res = Solution().reverseKGroup(list_to_linkedlist([1, 2, 3, 4, 5]), 2)
print(linkedlist_to_list(res))
res = Solution().reverseKGroup(list_to_linkedlist([1, 2, 3, 4, 5]), 3)
print(linkedlist_to_list(res))
