"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    formatters = ['({})', '{}()', '(){}']

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        else:
            ret = []
            combinations = self.generateParenthesis(n - 1)
            index = len(self.formatters) - 1
            for i, formatter in enumerate(self.formatters):
                if i == index:
                    ret.extend([formatter.format(combination) for combination in combinations[:-1]])
                else:
                    ret.extend([formatter.format(combination) for combination in combinations])

            return ret


def test(s):
    assert s.generateParenthesis(2) == ['(())', '()()']
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()()()", "()(())"]
    assert s.generateParenthesis(1) == ['()']
    assert s.generateParenthesis(0) == []
