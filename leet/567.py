"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down,
left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
from collections import defaultdict


class Solution:
    cache = defaultdict(int)

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.recurse(m, n, i, j, N) % (1e9 + 7)

    def recurse(self, m, n, i, j, N):
        if i < 0 or j < 0 or i == m or j == n:
            return 1

        if N == 0:
            return 0

        if (i, j, N) in self.cache:
            return self.cache[(i, j, N)]

        paths = 0
        N -= 1
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            paths += self.recurse(m, n, i + dx, j + dy, N)
        self.cache[(i, j, N)] = paths

        return paths


class SolutionV2:
    def findPaths(self, m, n, N, i, j, mod=1e9 + 7):
        dp = [[0] * n for _ in range(m)]
        pre_row, pre_col = None, None
        for _ in range(N):
            for r in range(m):
                tmp_row = dp[r].copy()
                for c in range(n):
                    tmp_col = dp[r][c]
                    dp[r][c] = (
                                   ((1 if r == 0 else pre_row[c])+(1 if c == 0 else pre_col)) +
                                   ((1 if r == m - 1 else dp[r+1][c]) + (1 if c == n - 1 else dp[r][c+1]))
                               ) % mod

                    pre_col = tmp_col
                pre_row = tmp_row

        return dp[i][j]


s = SolutionV2()
assert s.findPaths(2, 2, 1, 0, 0) == 2
assert s.findPaths(2, 2, 2, 0, 0) == 6
assert s.findPaths(1, 3, 3, 0, 1) == 12
assert s.findPaths(10, 10, 11, 5, 5)
