"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortest = None
        word1_loc, word2_loc = None, None
        for i, word in enumerate(words):
            if word == word1:
                word1_loc = i
                if word2_loc is None:
                    continue

                distance = i - word2_loc
            elif word == word2:
                word2_loc = i
                if word1_loc is None:
                    continue

                distance = i - word1_loc
            else:
                continue

            if not shortest or distance < shortest:
                shortest = distance

        return shortest


s = Solution()
assert s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice') == 3
assert s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding') == 1
