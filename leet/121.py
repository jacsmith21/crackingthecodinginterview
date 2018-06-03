"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

# Actions:
# buy and sell
# buy hold sell
import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        s0prev = 0
        s1prev = -sys.maxsize - 1
        s2prev = -sys.maxsize - 1

        for p in prices:
            s0 = max(s0prev, s2prev)
            s1 = max(s1prev, s0prev - p)
            s2 = max(s2prev, s1prev + p)
            s0prev = s0
            s1prev = s1
            s2prev = s2
            print()

        # noinspection PyUnboundLocalVariable
        return max(s0, s2)


s = Solution()
assert s.maxProfit([1, 2, 3, 0, 2]) == 3
assert s.maxProfit([1, 2, 0, 1]) == 1
assert s.maxProfit([1, 2, 0]) == 1
assert s.maxProfit([1]) == 0
assert s.maxProfit([1, 2, 5]) == 4
assert s.maxProfit([1, 2]) == 1
assert s.maxProfit([5, 4, 2, 0, 20]) == 20
assert s.maxProfit([3, 4, 0, 2, 20]) == 20
assert s.maxProfit([1, 0, 3, 3, 0, 2]) == 5
assert s.maxProfit([2, 3, 0, 2]) == 2
