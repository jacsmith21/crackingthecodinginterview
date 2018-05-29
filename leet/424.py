"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring
containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
import collections


class Solution:
    def characterReplacement(self, s, k):
        lo = hi = 0
        counts = collections.Counter()
        for i, c in enumerate(s):
            hi = i + 1
            counts[c] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo - max_char_n > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo


def test(s):
    assert s.characterReplacement('ACACCBCA', 2) == 6
    assert s.characterReplacement('IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR', 2) == 6
    assert s.characterReplacement('AABABBA', 1) == 4
    assert s.characterReplacement('ABAB', 2) == 4
    assert s.characterReplacement('', 4) == 0
    assert s.characterReplacement('A', 4) == 1
    assert s.characterReplacement('ABC', 4) == 3
