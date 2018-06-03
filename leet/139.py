"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    class Node:
        def __init__(self):
            self.children = {}

    def wordBreak(self, s, wordDict):
        ok = [False] * (len(s) + 1)
        ok[0] = True
        for i in range(1, len(s) + 1):
            ok[i] = any([ok[j] and s[j:i] in wordDict for j in range(i)])
        return ok[-1]

    def wordBreakV2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False

        start = self.Node()
        for word in wordDict:
            self.construct(word, 0, start, start)

        return self.dfs(s, 0, start, start)

    def construct(self, string, index, node, start):
        if index == len(string):
            node.children[start] = start
            return

        char = string[index]
        if char not in node.children:
            node.children[char] = self.Node()
        self.construct(string, index + 1, node.children[char], start)

    def dfs(self, string, index, node, start):
        if start in node.children:
            if index == len(string):
                return True
            else:
                if self.dfs(string, index, start, start):
                    return True

        if index >= len(string):
            return False

        if string[index] not in node.children:
            return False

        return self.dfs(string, index + 1, node.children[string[index]], start)


def test(s):
    assert s.wordBreak('aaaaaaa', {"aaaa", "aaa"})
    assert not s.wordBreak('leetcode', {})
    assert not s.wordBreak('aaaaaaa', {"aaaa", "aa"})
    assert s.wordBreak('aaaaaa', {"aaaa", "aa"})
    assert s.wordBreak('leetcode', {'leet', 'code'})
    assert s.wordBreak('leetcode', {'leet', 'code'})
    assert s.wordBreak('applepenapple', {'apple', 'pen'})
    assert not s.wordBreak('catsandog', {"cats", "dog", "sand", "and", "cat"})
