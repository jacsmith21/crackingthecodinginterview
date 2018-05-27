"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)
        while True:
            left = (start + end) // 2  # aka the actuall center
            right = left + 1

            if end - start <= 1:
                return nums[left]

            # if the left value is even
            if left % 2 == 0:
                if nums[left] != nums[right]:
                    end = left + 1
                else:
                    start = right + 1
            else:
                if nums[left] == nums[right]:
                    end = left
                else:
                    start = right


s = Solution()
assert s.singleNonDuplicate([1, 8, 8]) == 1
assert s.singleNonDuplicate([1, 1, 8]) == 8
assert s.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 8, 8]) == 4
assert s.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7]) == 5
assert s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
assert s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
