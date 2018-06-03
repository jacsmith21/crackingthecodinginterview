"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""


# Definition for an interval.
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return other[0] == self.start and other[1] == self.end


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda interval: interval.start)

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current.start <= merged[-1].end:
                if merged[-1].end < current.end:
                    merged[-1].end = current.end
            elif current:
                merged.append(current)

        return merged

    def attempt(self, intervals):
        return self.merge([Interval(*interval) for interval in intervals])


solution = Solution()
assert solution.attempt([[1, 4], [2, 3]]) == [[1, 4]]
assert solution.attempt([[1, 4], [0, 1]]) == [[0, 4]]
assert solution.attempt([[1, 4], [0, 4]]) == [[0, 4]]
assert solution.attempt([[1, 4], [4, 5]]) == [[1, 5]]
assert solution.attempt([[1, 3]]) == [[1, 3]]
assert solution.attempt([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
