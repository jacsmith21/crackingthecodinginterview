"""
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""
import bisect
import sys


class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        maxximum = None
        for row in range(m):
            for col in range(n):
                for i in range(row, m):
                    for j in range(col, n):
                        count = self.sum(matrix, row, i + 1, col, j + 1)
                        maxximum = count if maxximum is None or (maxximum < count <= k) else maxximum

                        if maxximum == k:
                            return maxximum
        else:
            return maxximum

    @staticmethod
    def sum(matrix, r1, r2, c1, c2):
        count = 0
        for i in range(r1, r2):
            for j in range(c1, c2):
                count += matrix[i][j]
        return count


class SolutionV2:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        best = -sys.maxsize - 1
        for left in range(n):
            summed = [0] * m
            for right in range(left, n):
                for i in range(m):
                    summed[i] += matrix[i][right]

                largest = self.largest_sum_sub_array_le_k(summed, k)
                best = max(best, largest)

        print(best)
        return best

    @staticmethod
    def largest_sum_sub_array_le_k(arr, k):
        cum, best = 0, -sys.maxsize - 1
        values = [0]
        for element in arr:
            cum += element
            index = bisect.bisect_left(values, cum - k)

            if index < len(values):
                sum = cum - values[index]
                best = sum if sum > best else best

            bisect.insort(values, cum)

        return best


s = SolutionV2()
assert s.maxSumSubmatrix([
    [1, 0, 1],
    [0, -2, 3]], 2) == 2

assert s.maxSumSubmatrix(
    [[1, 0, 3],
     [0, -2, 5]], 2) == 1

assert s.maxSumSubmatrix([[2, 1, -3, -4, 5],
                          [0, 6, 3, 4, 1],
                          [2, -2, -1, 4, -5],
                          [-3, 3, 1, 0, 3]], 18) == 18

assert s.maxSumSubmatrix([[2, 2, -1]], 0) == -1
