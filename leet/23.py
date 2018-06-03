"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
import heapq

import leet


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        ret = []
        queue = [(start.val, i) for i, start in enumerate(lists) if start is not None]
        heapq.heapify(queue)
        while queue:
            value, index = heapq.heappop(queue)
            ret.append(value)
            if lists[index].next is not None:
                heapq.heappush(queue, (lists[index].next.val, index))
                lists[index] = lists[index].next

        return ret


def test(s):
    assert s.mergeKLists([leet.make([1, 4, 5]), leet.make([1, 3, 4]), leet.make([2, 6])]) == [1, 1, 2, 3, 4, 4, 5, 6]
