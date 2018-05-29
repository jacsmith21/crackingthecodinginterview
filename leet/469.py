"""
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:
There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex,
and that edges otherwise don't intersect each other.
"""


class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        prev_cross_product = 0
        for i, point in enumerate(points):
            prev_point = points[i - 1]
            next_point = points[(i + 1) % len(points)]
            dx1, dy1 = self.d(point, prev_point)
            dx2, dy2 = self.d(next_point, point)
            cross_product = dx1 * dy2 - dx2 * dy1

            if cross_product != 0:
                if cross_product * prev_cross_product < 0:
                    return False
                else:
                    prev_cross_product = cross_product

        return True

    @staticmethod
    def d(p1, p2):
        return p1[0] - p2[0], p1[1] - p2[1]


s = Solution()
assert s.isConvex([[0, 0], [0, 1], [1, 1], [1, 0]])
assert s.isConvex([[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]])
assert not s.isConvex([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]])
assert not s.isConvex([[0, 0], [0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3], [3, 0]])
