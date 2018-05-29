"""
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"

Note:
The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1,10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""
import math
import re


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        class Fraction:
            def __init__(self, n, d):
                self.n = n
                self.d = d

        fractions = []
        regex = re.compile(r'([+-])?(\d+)/(\d+)')
        denominators = set()
        for (sign, numerator, denominator) in regex.findall(expression):
            fractions.append(Fraction(int(numerator), int(denominator)))

            if sign == '-':
                fractions[-1].n *= -1
            denominators.add(fractions[-1].d)

        common = 1
        for denominator in denominators:
            common *= denominator

        summed = 0
        for fraction in fractions:
            summed += fraction.n * common / fraction.d

        numerator = summed
        denominator = common
        common = math.gcd(int(numerator), int(denominator))

        return '{}/{}'.format(int(numerator / common), int(denominator / common))


s = Solution()
assert s.fractionAddition('7/3+5/2-3/10') == '68/15'
assert s.fractionAddition('-1/2+1/2') == '0/1'
assert s.fractionAddition('-1/2+1/2+1/3') == '1/3'
assert s.fractionAddition('1/3-1/2') == '-1/6'
assert s.fractionAddition('5/3+1/3') == '2/1'
