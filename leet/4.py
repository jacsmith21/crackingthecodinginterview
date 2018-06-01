"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = 0, 0
        r1, r2 = len(nums1), len(nums2)
        while True:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            if m1 < m2:
                pass


def test(s):
    s.findMedianSortedArrays([1, 3], [2]) == 2
    s.findMedianSortedArrays([1, 3, 4, 6], [0, 1, 2]) == 2
    s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
