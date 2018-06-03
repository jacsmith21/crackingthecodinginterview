"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort = sorted(nums)
        lesser = 0
        greater = len(sort) - 1
        while lesser < greater:
            number = sort[greater] + sort[lesser]
            if target == number:
                first = None
                for i, num in enumerate(nums):
                    if num == sort[greater] or num == sort[lesser]:
                        if first is None:
                            first = i
                        else:
                            return [first, i]
                raise Exception
            elif target < number:
                greater -= 1
            else:
                lesser += 1

        raise Exception


s = Solution()
assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
