"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        node = self
        for val in other:
            if node is None or val != node.val:
                return False
            else:
                node = node.next
        return True


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if l1 is None and l2 is None:
            return None if carry is 0 else ListNode(carry)
        elif l1 is None:
            carry, val = divmod(l2.val + carry, 10)
            node = ListNode(val)
            node.next = self.addTwoNumbers(l1, l2.next, carry=carry)
        elif l2 is None:
            carry, val = divmod(l1.val + carry, 10)
            node = ListNode(val)
            node.next = self.addTwoNumbers(l1.next, l2, carry=carry)
        else:
            carry, val = divmod(l1.val + l2.val + carry, 10)
            node = ListNode(val)
            node.next = self.addTwoNumbers(l1.next, l2.next, carry=carry)
        return node


def test(s):
    def make(nums):
        start = ListNode(nums[0])
        node = start
        for n in nums[1:]:
            node.next = ListNode(n)
            node = node.next
        return start

    assert s.addTwoNumbers(make([9, 9]), make([1])) == [0, 0, 1]
    assert s.addTwoNumbers(make([5]), make([5])) == [0, 1]
    assert s.addTwoNumbers(make([2, 4, 3]), make([5, 6, 4, 1, 6])) == [7, 0, 8, 1, 6]
    assert s.addTwoNumbers(make([2]), None) == [2]
