"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        class Node:
            def __init__(self):
                self.children = {}

        auto = Node()
        start = node = Node()
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == '*':
                node.children[p[i]] = node
                node.children[auto] = Node()
                node = node.children[auto]
                i += 2
            else:
                node.children[p[i]] = Node()
                node = node.children[p[i]]
                i += 1

        return self.recurse(s, 0, start, auto)

    def recurse(self, s, i, node, auto):
        if len(s) == i:
            if auto in node.children and not node.children[auto].children:
                return True
            elif not node.children:
                return True
            else:
                return False
        if auto in node.children and self.recurse(s, i, node.children[auto], auto):
            return True

        if (s[i] in node.children or s[i] == '.') and self.recurse(s, i + 1, node.children[s[i]], auto):
            return True

        return False


def test(s):
    assert not s.isMatch('aa', 'a')
    assert s.isMatch('', 'a*')
    assert not s.isMatch('a', 'b')
    assert s.isMatch('a*b*c*', 'abc')
    assert s.isMatch('a', 'a*')
    assert s.isMatch('a', 'a*')
    assert s.isMatch('aaaa', 'a*')
    assert s.isMatch('aaaa', 'aa*a')
    assert s.isMatch('aaaab', 'a*b')
    assert s.isMatch('b', 'a*b')
