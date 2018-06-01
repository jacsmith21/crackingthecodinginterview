"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        if n <= 0:
            return False

        while n != 1:
            n, rem = divmod(n, 2)
            if rem != 0:
                return False

        return True


def test(s):
    assert s.isPowerOfTwo(1)
    assert s.isPowerOfTwo(2)
    assert s.isPowerOfTwo(4)
    assert s.isPowerOfTwo(16)
    assert not s.isPowerOfTwo(218)
    assert not s.isPowerOfTwo(15)


