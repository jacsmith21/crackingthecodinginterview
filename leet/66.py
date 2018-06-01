"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits, index=None, amount=1):
        """
        :type digits: List[int]
        :rtype: List[int]
        :param index:
        :param amount:
        """
        if amount == 0:
            return

        index = index if index is not None else len(digits) - 1
        if index == -1:
            index = 0
            digits.insert(0, 0)

        digits[index] += amount
        amount = digits[index] // 10
        digits[index] %= 10
        self.plusOne(digits, index - 1, amount)

        return digits


def test(s):
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
