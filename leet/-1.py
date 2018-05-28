"""
Find the largest sum within a given sub-array. You can assume there is at least one positive number.

Example:
In: [1, 2, -2, 0, 1]
Out: 3
"""


class Solution:
    @staticmethod
    def largest_sum_sub_array(arr):
        max_so_far, max_ending_here = 0, 0
        for element in arr:
            max_ending_here += element
            max_ending_here = 0 if max_ending_here < 0 else max_ending_here
            max_so_far = max_ending_here if max_ending_here > max_so_far else max_so_far

        return max_so_far


s = Solution()
assert s.largest_sum_sub_array([1, 2, -1, 0, 1]) == 3
assert s.largest_sum_sub_array([1, 2, -1, 1, 1]) == 4
assert s.largest_sum_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

