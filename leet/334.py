"""

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
"""
import sys


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest, ssmallest = sys.maxsize, sys.maxsize
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= ssmallest:
                ssmallest = n
            else:
                return True
        else:
            return False


def test(s):
    assert s.increasingTriplet([1, 2, 3, 4, 5])
    assert not s.increasingTriplet([1, 4, 3, 3, 2])
    assert not s.increasingTriplet([1, 2, 2, 1, 2])
    assert not s.increasingTriplet([5, 4, 3, 2, 1])
