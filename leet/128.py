"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longest = 0
        seen = set()
        for num in nums:
            count = self.count(num, nums, seen)
            longest = count if count > longest else longest

        return longest

    def count(self, num, nums, seen):
        if num not in nums or num in seen:
            return 0

        seen.add(num)
        return 1 + self.count(num - 1, nums, seen) + self.count(num + 1, nums, seen)


def test(s):
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0]) == 1
    assert s.longestConsecutive([]) == 0
