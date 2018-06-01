"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
import collections


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening = {'{', '[', '('}
        closing = {'}', ']', ')'}
        mapping = {'}': '{', ']': '[', ')': '('}
        stack = collections.deque()
        for c in s:
            if c in closing:
                if not stack:
                    return False

                opening_bracket = stack.pop()
                if opening_bracket != mapping[c]:
                    return False
            elif c in opening:
                stack.append(c)

        if stack:
            return False

        return True


def test(s):
    assert s.isValid('{}[]()')
    assert s.isValid('{()[]}')
    assert not s.isValid('([)]')
    assert not s.isValid('({)[]}')
    assert not s.isValid('{[}')
    assert not s.isValid(']')
    assert not s.isValid('[')
