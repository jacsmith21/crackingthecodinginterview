"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that
your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = -1 if x < 0 else 1
        x = abs(x)
        num = neg * int(''.join([c for c in reversed(str(x))]))
        num = 0 if num < -2 ** 31 or num > 2 ** 31 - 1 else num
        return num


def test(s):
    assert s.reverse(1534236469) == 0
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
