"""
Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
"""
from structures import Stack


def sort(stack):
    temp = Stack()

    count = None
    while True:
        maximum = stack.pop()
        i = 1
        while not stack.empty():
            if count is not None and i >= count:
                break

            node = stack.pop()
            if node > maximum:
                node, maximum = maximum, node

            temp.push(node)
            i += 1

        count = 0
        stack.push(maximum)
        while not temp.empty():
            stack.push(temp.pop())
            count += 1

        if count == 0:
            break


s = Stack(1, 4, 2, 3)
sort(s)
assert s == (4, 3, 2, 1)
