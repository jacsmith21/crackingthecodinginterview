"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = [int(d) - 2 for d in digits]
        return self.combinations(digits)

    def combinations(self, digits, index=0):
        if index == len(digits):
            return []

        if index == len(digits) - 1:
            return list(self.mapping[digits[index]])

        ret = []
        for comb in self.combinations(digits, index + 1):
            ret.extend([c + comb for c in self.mapping[digits[index]]])

        return ret


def test(s):
    expected = {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
    for combination in s.letterCombinations('23'):
        assert combination in expected

    assert s.letterCombinations([]) == []
