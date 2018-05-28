"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.
"""
from collections import defaultdict


class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        d = defaultdict(set)
        x_max = None
        x_min = None
        for [x, y] in points:
            d[x].add(y)
            x_max = x if x_max is None or x > x_max else x_max
            x_min = x if x_min is None or x < x_min else x_min
        mid = (x_min + x_max) / 2

        for [x, y] in points:
            counterpart = 2 * mid - x, y
            if counterpart[1] not in d[counterpart[0]]:
                return False

        return True


s = Solution()
assert s.isReflected([[1, 2], [2, 2], [1, 4], [2, 4]])
assert s.isReflected([[0, 0], [0, 0]])
assert not s.isReflected([[1, 1], [-1, -1]])
assert s.isReflected([[-16, 1], [16, 1], [16, 1]])
assert s.isReflected([[1, 2], [2, 2], [3, 2], [4, 2]])
assert s.isReflected([[1, 1], [-1, 1]])
assert s.isReflected([[1, 1], [-1, 1], [0, -200]])
