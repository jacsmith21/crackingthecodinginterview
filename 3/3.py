"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop ( ) should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
"""
from structures import Stack, EmptyException


class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [Stack()]

    @property
    def count(self):
        return len(self.stacks[-1])

    def push(self, data):
        if self.threshold == self.count:
            self.stacks.append(Stack())

        self.stacks[-1].push(data)

    def pop(self):
        try:
            return self.stacks[-1].pop()
        except EmptyException:
            self.stacks = self.stacks[:-1]
            return self.pop()
        except IndexError:
            raise EmptyException

    def pop_at(self, i):
        return self.stacks[i].pop()


stack = SetOfStacks(2)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

assert 5 == stack.pop()
assert 2 == stack.pop_at(0)
assert 4 == stack.pop()
assert 3 == stack.pop()
assert 1 == stack.pop()
