"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    class ParseException(Exception):
        pass

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [int(digit) for digit in s]
        return self.recurse(s, 0, {})

    def recurse(self, s, start, lookup):
        if len(s) - start == 0:
            return 0

        if s[start] == 0:
            return 0

        if len(s) - start == 1:
            return 1

        if start in lookup:
            return lookup[start]

        combinations = self.recurse(s, start + 1, lookup)

        if start + 1 < len(s):
            if 0 < s[start] * 10 + s[start + 1] <= 26:
                if len(s) - start == 2:
                    combinations += 1
                else:
                    combinations += self.recurse(s, start + 2, lookup)

        lookup[start] = combinations
        return combinations


s = Solution()
assert s.numDecodings("12") == 2
assert s.numDecodings("01") == 0
assert s.numDecodings("10") == 1
assert s.numDecodings("101") == 1
assert s.numDecodings("226") == 3
assert s.numDecodings("2117") == 5
