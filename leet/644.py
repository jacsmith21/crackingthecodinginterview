"""
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the
maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""
import numpy as np
import tensortools.testing as tt


class SolutionV2:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        r, l = 10000, -10000
        while r - l > 0.000004:
            mid = (l + r) / 2
            if self.check(nums, k, mid):
                l = mid
            else:
                r = mid
        return r

    @staticmethod
    def check(nums, k, x):
        n = len(nums)
        a = [0.0] * n
        for i in range(n):
            a[i] = nums[i] - x

        now, last = 0, 0
        for i in range(k):
            now += a[i]

        if now >= 0:
            return True

        for i in range(k, n):
            now += a[i]
            last += a[i - k]
            if last < 0:
                now -= last
                last = 0
            if now >= 0:
                return True

        return False


class Solution:
    def findMaxAverage(self, nums, k):
        lo, hi = min(nums), max(nums)
        nums = np.array([0] + nums)
        while hi - lo > 1e-5:
            mid = nums[0] = (lo + hi) / 2.
            sums = (nums - mid).cumsum()
            mins = np.minimum.accumulate(sums)
            if (sums[k:] - mins[:-k]).max() > 0:
                lo = mid
            else:
                hi = mid
        return lo


def test(s):
    assert tt.approx(s.findMaxAverage([1, 12, -5, -6, 50, 3], k=4), 12.75)
