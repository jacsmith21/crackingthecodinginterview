"""
Largest sum subarray with at-least k numbers
Given an array, find the subarray (containing at least k numbers) which has the largest sum.

Examples:

Input : arr[] = {-4, -2, 1, -3}
            k = 2
Output : -1
The sub array is {-2, 1}

Input : arr[] = {1, 1, 1, 1, 1, 1}
            k = 2
Output : 6
The sub array is {1, 1, 1, 1, 1, 1}
"""


def max_sum_subarray_at_least_k(arr, k):
    return 0


def test():
    assert max_sum_subarray_at_least_k([-4, -2, 1, -3], 2) == -1
    assert max_sum_subarray_at_least_k([1, 1, 1, 1, 1], 2) == 5
