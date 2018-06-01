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
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False

        start = self.Node()
        for word in wordDict:
            prev = start
            for c in word:
                if c in prev.children:
                    prev = prev.children[c]
                else:
                    prev.children[c] = [self.Node()]
                    prev = prev.children[c][0]

        return self.dfs(s, 0, start, start)

    def construct(self, string, index, node):
        char = string[index]
        if char in node.children:
            for child in node.children[char]:
                if self.construct(string, index + 1, child):
                    break
            else:
                node.children[char].append(self.Node())
                return True

        else:
            node.children[char] = [self.Node()]
            return True

    def dfs(self, string, index, node, start):
        if not node.children:
            if index == len(string):
                return True
            else:
                return self.dfs(string, index, start, start)

        if len(string) <= index:
            return False

        if string[index] not in node.children:
            return False

        for child in node.children[string[index]]:
            if not self.dfs(string, index + 1, child, start):
                continue
            else:
                return True
        else:
            return False


def test(s):
    assert not s.wordBreak('leetcode', {})
    assert not s.wordBreak('aaaaaaa', {"aaaa", "aa"})
    assert s.wordBreak('aaaaaa', {"aaaa", "aa"})
    assert s.wordBreak('leetcode', {'leet', 'code'})
    assert s.wordBreak('leetcode', {'leet', 'code'})
    assert s.wordBreak('applepenapple', {'apple', 'pen'})
    assert not s.wordBreak('catsandog', {"cats", "dog", "sand", "and", "cat"})
