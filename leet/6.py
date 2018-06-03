"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
import math


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index = 0
        result = [''] * len(s)
        interval = numRows + max(numRows - 2, 0)
        n_intervals = int(math.ceil(len(s) / interval))
        for i in range(numRows):
            for j in range(0, interval * n_intervals + 1, interval):
                if j != 0 < i < numRows - 1 and j - i < len(s):
                    result[index] = s[j - i]
                    index += 1
                if j + i < len(s):
                    result[index] = s[j + i]
                    index += 1

        return ''.join(result)


def test(s):
    assert s.convert('ABC', 1) == 'ABC'
    assert s.convert('', 1) == ''
    assert s.convert('P', 3) == 'P'
    assert s.convert('', 3) == ''
    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
