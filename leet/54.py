"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        class Result:
            def __init__(self, matrix):
                self.result = [0] * (len(matrix) * len(matrix[0]))
                self.index = 0

            def append(self, value):
                self.result[self.index] = value
                self.index += 1

        self.m = len(matrix) - 1
        self.n = len(matrix[0]) - 1
        res = Result(matrix)
        self.recurse(matrix, 0, res)
        return res.result

    def recurse(self, matrix, level, res):
        if level > self.n - level or level > self.m - level:
            return

        if level == self.n - level and level == self.m - level:
            res.append(matrix[level][level])
        elif level == self.n - level:
            for i in range(level, self.m - level + 1):
                res.append(matrix[i][level])
        elif level == self.m - level:
            for j in range(level, self.n - level + 1):
                res.append(matrix[level][j])
        else:
            for j in range(level, self.n - level):
                res.append(matrix[level][j])
            for i in range(level, self.m - level):
                res.append(matrix[i][self.n - level])
            for j in range(self.n - level, level, -1):
                res.append(matrix[self.m - level][j])
            for i in range(self.m - level, level, -1):
                res.append(matrix[i][level])
            self.recurse(matrix, level + 1, res)


def test(s):
    assert s.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert s.spiralOrder([[6, 9, 7]]) == [6, 9, 7]
    assert s.spiralOrder([]) == []
    assert s.spiralOrder([[]]) == []
    assert s.spiralOrder([[1]]) == [1]
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
