"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_count = 0
        max_left = 0
        max_right = 0
        for center in range(len(s) * 2 - 1):
            if center % 2 == 0:
                left = center // 2 - 1
                right = center // 2 + 1
                count = 1
            else:
                left = center // 2
                right = left + 1
                count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 2
                left -= 1
                right += 1
            else:
                if count > max_count:
                    max_count = count
                    max_left = left + 1
                    max_right = right - 1

        return s[max_left:max_right + 1]


def test(s):
    assert s.longestPalindrome('babad') == 'bab'
    assert s.longestPalindrome('cbbd') == 'bb'
