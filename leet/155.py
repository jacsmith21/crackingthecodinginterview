"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
import collections


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = collections.deque()
        self._mins = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self._mins or x <= self.getMin():
            self._mins.append(x)
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self._stack.pop()
        if value == self.getMin():
            self._mins.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._mins[-1]


def test():
    obj = MinStack()
    obj.push(85)
    obj.push(-99)
    obj.push(67)
    assert obj.getMin() == -99
    obj.pop()
    obj.pop()
    obj.pop()

    obj.push(0)
    obj.push(1)
    obj.push(0)
    assert obj.getMin() == 0
    assert obj.pop() == 0
    assert obj.getMin() == 0
    obj.pop()
    obj.pop()

    obj.push(5)
    obj.push(6)
    assert obj.getMin() == 5
    obj.push(3)
    assert obj.getMin() == 3
    assert obj.pop() == 3
    assert obj.top() == 6
    assert obj.getMin() == 5
