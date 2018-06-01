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
    max_sums = [0 for _ in arr]
    max_sums[0] = arr[0]
    for i in range(1, len(arr)):
        max_sums[i] = max(arr[i], max_sums[i - 1] + arr[i])

    c_sum = 0
    for i in range(k):
        c_sum += arr[i]

    max_sum = c_sum
    for i in range(k, len(arr)):
        c_sum = c_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, c_sum, c_sum + max_sums[i - k])

    return max_sum


def test():
    assert max_sum_subarray_at_least_k([1, 1, 1, 1, 1], 2) == 5
    assert max_sum_subarray_at_least_k([-4, -2, 1, -3], 2) == -1
    assert max_sum_subarray_at_least_k([1, 2, 3, -10, -3], 4) == -4
