"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1, version2 = [[int(revision) for revision in version.split('.')] for version in [version1, version2]]
        i = 0
        for i, (revision1, revision2) in enumerate(zip(version1, version2)):
            if revision1 < revision2:
                return -1
            elif revision1 > revision2:
                return 1

        i += 1
        while i < len(version1):
            if version1[i] != 0:
                return 1
            i += 1

        while i < len(version2):
            if version2[i] != 0:
                return -1
            i += 1

        return 0


def test(s):
    assert s.compareVersion('01', '1') == 0
    assert s.compareVersion('1.1', '1.10') == -1
    assert s.compareVersion('0.1', '1.1') == -1
    assert s.compareVersion('1.0', '1') == 0
    assert s.compareVersion('1.0.1', '1') == 1
    assert s.compareVersion('7.5.2.4', '7.5.3') == -1
