"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""
from structures import List

lst = List(1, 2, 3, 4, 5, 6, 7)

k = 5

el = None
for i, n in enumerate(lst):
    if i == (k - 1):
        el = lst.head
    elif i > (k - 1):
        el = el.next


assert el == 3
