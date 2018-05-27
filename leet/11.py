"""

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries,
return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are
positive. This represents the equations. Return vector<double>.

Example:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
"""
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        lookup = defaultdict(lambda: defaultdict(float))
        for [c1, c2], value in zip(equations, values):
            lookup[c1][c2] = value  # c1 / c2 = value
            lookup[c2][c1] = 1 / value  # c2 / c1 =  1 / value

        outputs = [self.search(query[0], query[1], lookup, defaultdict(bool)) for query in queries]
        return [output[1] for output in outputs]

    def search(self, start, target, lookup, seen):
        if seen[start]:
            return False, -1
        else:
            seen[start] = True

        for key in lookup[start]:
            if key == target:
                return True, lookup[start][key]
            else:
                found, res = self.search(key, target, lookup, seen)
                if not found:
                    continue
                return True, lookup[start][key] * res
        else:
            return False, -1


s = Solution()
assert s.calcEquation([["a", "b"], ["b", "c"]], [2, 3], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6, 0.5, -1, 1, -1]
