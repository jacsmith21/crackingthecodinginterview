"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
"""


class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        combinations = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}

        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in combinations or combinations[num[left]] != num[right]:
                return False

            right -= 1
            left += 1

        return True


def test(s):
    assert s.isStrobogrammatic('69')
    assert s.isStrobogrammatic('88')
    assert s.isStrobogrammatic('11')
    assert not s.isStrobogrammatic('692')
