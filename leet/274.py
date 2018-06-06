"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        counts = [0] * (len(citations) + 1)
        for citation in citations:
            counts[min(citation, len(citations))] += 1

        count = 0
        for i in reversed(range(len(counts))):
            count += counts[i]
            if count >= i:
                return i
        else:
            return -1


def test(s):
    assert s.hIndex([3, 0, 6, 1, 5]) == 3
