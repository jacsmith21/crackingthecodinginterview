"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
from collections import defaultdict


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'Node({})'.format(self.val)

    def __repr__(self):
        return 'Node({})'.format(self.val)

    @staticmethod
    def make(*nums):
        start = None
        prev = None
        for num in nums:
            node = ListNode(num)
            if prev is None:
                prev = node
                start = node
                continue

            prev.next = node
            prev = node

        return start


class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.recurse(head, defaultdict(bool))

    def recurse(self, head, seen):
        if head is None:
            return False
        elif seen[head]:
            return True
        else:
            seen[head] = True
            return self.recurse(head.next, seen)


def test(s):
    l = ListNode.make(0, 1, 2, 3, 4)
    assert not s.hasCycle(l)
    l.next.next.next.next.next = l.next
    assert s.hasCycle(l)
