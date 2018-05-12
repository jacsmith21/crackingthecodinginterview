"""
Implement a MyQueue class which implements a queue using two stacks.
"""
from structures import Stack, EmptyException


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.end_first = True

    def add(self, data):
        if self.end_first:
            self.s1.push(data)
        else:
            self.transfer()
            self.add(data)

    def remove(self):
        if self.end_first:
            self.transfer()
            return self.remove()
        else:
            return self.s2.pop()

    def transfer(self):
        try:
            if self.end_first:
                while True:
                    self.s2.push(self.s1.pop())
            else:
                while True:
                    self.s1.push(self.s2.pop())
        except EmptyException:
            self.end_first = not self.end_first


queue = MyQueue()
queue.add(5)
queue.add(2)
assert 5 == queue.remove()

queue.add(1)
assert 2 == queue.remove()
assert 1 == queue.remove()
