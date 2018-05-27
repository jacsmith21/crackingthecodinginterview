"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21


Example 2:
Input: 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = [int(d) for d in str(n)]
        lookup = {}
        previous = None
        for i in reversed(range(len(n))):
            digit = n[i]

            if previous is not None and digit < previous:
                break

            previous = digit
            lookup[digit] = i
        else:
            return -1

        for j in range(digit + 1, 10):
            if j not in lookup:
                continue

            index = lookup[j]
            n[i], n[index] = n[index], n[i]

            n[i + 1:] = sorted(n[i + 1:])

            res = 0
            power = 0
            for k in reversed(range(len(n))):
                res += 10 ** power * n[k]
                power += 1

            if res <= 2147483647:
                return res
            else:
                return -1


s = Solution()
assert s.nextGreaterElement(12) == 21
assert s.nextGreaterElement(21) == -1
assert s.nextGreaterElement(123) == 132
assert s.nextGreaterElement(341) == 413
assert s.nextGreaterElement(465) == 546
assert s.nextGreaterElement(4655) == 5456
