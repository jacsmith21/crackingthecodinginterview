"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)
        odd = False
        for count in counter:
            if counter[count] % 2 == 0:
                continue

            if odd:
                return False

            odd = True

        return True


def test(s):
    assert not s.canPermutePalindrome('code')
    assert s.canPermutePalindrome('aab')
    assert s.canPermutePalindrome('carerac')
    assert s.canPermutePalindrome('')
    assert s.canPermutePalindrome('1')
