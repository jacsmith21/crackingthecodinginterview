"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
from structures import List


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        i = 1
        prev = None
        curr = head
        while i != m:
            prev = curr
            curr = curr.next
            i += 1

        one_before = prev  # one before the start of the reverse
        new_end = curr  # the new end of the given interval

        nxt = curr.next
        while i != n:
            nxt.next, curr, nxt = curr, nxt, nxt.next
            i += 1

        new_end.next = nxt

        if one_before is not None:
            one_before.next = curr
            return head
        else:
            return curr


s = Solution()
assert s.reverseBetween(List(1, 2, 3, 4, 5).head, 3, 4) == [1, 2, 4, 3, 5]
