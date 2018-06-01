"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
import numpy as np


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = np.asarray(nums)

        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        else:
            nums.sort()
            return nums

        minimum = len(nums) - 1
        for j in range(len(nums) - 2, i, -1):
            minimum = nums[j] if nums[j] < nums[minimum] else minimum

        nums[i], nums[minimum] = nums[minimum], nums[i]
        nums[:i].sort()

        return nums


def test(s):
    assert (s.nextPermutation([3, 2, 1]) == [1, 2, 3]).all()
    assert (s.nextPermutation([1, 2, 3]) == [1, 3, 2]).all()
    assert (s.nextPermutation([1, 3, 2]) == [2, 1, 3]).all()
    assert (s.nextPermutation([1, 1, 5]) == [1, 5, 1]).all()
    assert (s.nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4]).all()
    assert (s.nextPermutation([1, 4, 5, 2]) == [1, 5, 2, 4]).all()
