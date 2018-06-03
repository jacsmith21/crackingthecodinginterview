"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        ret = '-' if (numerator < 0) ^ (denominator < 0) else ''
        num, dem = abs(numerator), abs(denominator)
        ret += str(num // dem)

        if num / dem % 1 == 0:
            return ret
        else:
            num = num % dem
            ret += '.'

        seen = {}
        fractions = []
        while num != 0:
            num *= 10

            if num in seen:
                fractions.insert(seen[num], '(')
                fractions.append(')')
                break
            else:
                seen[num] = len(fractions)
                fraction, num = divmod(num, dem)
                fractions.append(fraction)

        ret += ''.join([str(fraction) for fraction in fractions])
        return ret


def test(s):
    assert s.fractionToDecimal(1, 6) == '0.1(6)'
    assert s.fractionToDecimal(1, 333) == '0.(003)'
    assert s.fractionToDecimal(2, 2) == '1'
    assert s.fractionToDecimal(2, -2) == '-1'
    assert s.fractionToDecimal(1, 2) == '0.5'
    assert s.fractionToDecimal(2, 1) == '2'
    assert s.fractionToDecimal(2, 3) == '0.(6)'
    assert s.fractionToDecimal(5, 9) == '0.(5)'
    assert s.fractionToDecimal(23, 99) == '0.(23)'
