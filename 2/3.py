"""
Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
"""
from structures import List

lst = List(1, 2, 3, 4, 5)
n = lst[2]

lst.remove(n)

assert lst == (1, 2, 4, 5)
