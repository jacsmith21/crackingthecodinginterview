"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = dict()
        largest = 0
        start = 0
        for i, c in enumerate(s):
            if c in chars and chars[c] >= start:
                start = chars[c] + 1

            chars[c] = i
            length = i - start + 1
            largest = length if length > largest else largest
        return largest


def test(s):
    assert s.lengthOfLongestSubstring('abcbcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
