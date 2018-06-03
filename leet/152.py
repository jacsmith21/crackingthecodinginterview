"""

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    def maxProduct(self, nums):
        maxima = nums[0]
        local_min = nums[0]
        local_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num > 0:
                local_max, local_min = max(local_max * num, num), min(local_min * num, num)
            else:
                local_max, local_min = max(local_min * num, num), min(local_max * num, num)
            maxima = max(maxima, local_max)

        return maxima


s = Solution()
assert 6 == s.maxProduct([2, 3, -2, 4])
assert 0 == s.maxProduct([-2, 0, -1])
assert 1008 == s.maxProduct([1, -3, -5, -2, 0, 4, 9, 0, 3, -8, 7, -6])
assert 48 == s.maxProduct([0, 3, -2, 4, -2])
