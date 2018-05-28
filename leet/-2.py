"""
Find the largest sum within a given sub-array that is less than or equal to a value k. You can assume there is at least one positive number.

Example:
In: [1, 2, -2, 0, 1]
Out: 3
"""
import bisect


class Solution:
    @staticmethod
    def largest_sum_sub_array_le_k(arr, k):
        cum, best = 0, 0
        values = [0]
        for element in arr:
            cum += element
            index = bisect.bisect_left(values, cum - k)

            if index < len(values):
                sum = cum - values[index]
                best = sum if sum > best else best

            bisect.insort(values, cum)

        return best


s = Solution()
assert s.largest_sum_sub_array_le_k([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
assert s.largest_sum_sub_array_le_k([1, 2, -1, 0, 1], 3) == 3
assert s.largest_sum_sub_array_le_k([1, 2, -1, 1, 1], 3) == 3
assert s.largest_sum_sub_array_le_k([1, -2, -1, 4, 3], 2) == 2
