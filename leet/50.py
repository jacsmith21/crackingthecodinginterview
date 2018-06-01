"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
import tensortools.testing as tt


class Solution:
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n

    def myPow(self, x, n):
        ret = 1
        for _ in range(n):
            ret *= x
        return ret


def test(s):
    assert tt.approx(s.myPow(2, 10), 1024)
    assert tt.approx(s.myPow(2.1, 3), 9.2610)
