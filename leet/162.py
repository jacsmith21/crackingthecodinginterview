"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r - 1:
            c = (l + r) // 2
            if nums[c - 1] < nums[c] > nums[c + 1]:
                return c
            elif nums[c - 1] < nums[c]:
                l = c + 1
            else:
                r = c

        return l if nums[l] > nums[r] else r

    def findPeakElementV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        else:
            raise Exception


def test(s):
    assert s.findPeakElement([1]) == 0
    assert s.findPeakElement([1, 2]) == 1
    assert s.findPeakElement([2, 1]) == 0
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in {1, 5}
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 3, 1]) == 1
