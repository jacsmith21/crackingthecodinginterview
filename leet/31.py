"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while nums[i - 1] >= nums[i]:
            i -= 1
            if i <= 0:
                break
        else:
            i -= 1  # going to the first number < than the next number
            for j in range(len(nums) - 1, i, -1):  # check every number but not i
                if nums[j] > nums[i]:
                    break
            else:
                raise Exception('this shouldn\'t happen')

            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        self.reverse(nums, i, len(nums) - 1)
        return nums

    @staticmethod
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


def test(s):
    nums = [1, 2, 3, 4]
    s.reverse(nums, 0, len(nums) - 1)
    assert nums == [4, 3, 2, 1]
    assert (s.nextPermutation([3, 2, 1]) == [1, 2, 3])
    assert (s.nextPermutation([1, 2, 3]) == [1, 3, 2])
    assert (s.nextPermutation([1, 3, 2]) == [2, 1, 3])
    assert (s.nextPermutation([1, 1, 5]) == [1, 5, 1])
    assert (s.nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4])
    assert (s.nextPermutation([1, 4, 5, 2]) == [1, 5, 2, 4])
