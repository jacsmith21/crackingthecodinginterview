"""
Sliding Window Maximum (Maximum of all subarrays of size k)
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples :

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6



Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90
"""


def max_sums_at_k(arr, k):
    return []


def test():
    assert max_sums_at_k([1, 2, 3, 1, 4, 5, 2, 3, 6], 3) == [3, 3, 4, 5, 5, 5, 6]
    assert max_sums_at_k([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4) == [10, 10, 10, 15, 15, 90, 90]
