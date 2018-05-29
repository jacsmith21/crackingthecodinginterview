"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.higher = []
        self.lower = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.lower or num < -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)

        if len(self.lower) - len(self.higher) > 1:
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        elif len(self.higher) - len(self.lower) > 1:
            heapq.heappush(self.lower, -heapq.heappop(self.higher))

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.lower) + len(self.higher)) % 2 == 0:
            return (-self.lower[0] + self.higher[0]) / 2
        else:
            if len(self.lower) > len(self.higher):
                return -self.lower[0]
            else:
                return self.higher[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def test():
    m = MedianFinder()

    m.addNum(1)
    m.addNum(2)
    assert m.findMedian() == 1.5

    m.addNum(3)
    m.addNum(4)
    assert m.findMedian() == 2.5

    m.addNum(4)
    assert m.findMedian() == 3

    m.addNum(5)
    m.addNum(10)
    assert m.findMedian() == 4

