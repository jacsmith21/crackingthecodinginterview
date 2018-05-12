"""
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.

EXAMPLE
Input: A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
Output: C
"""
from structures import List


def start_of_loop(ll):
    seen = []
    for n in ll:
        if id(n) in seen:
            return n
        else:
            seen.append(id(n))
    else:
        return None


lst = List(1, 2, 3, 4)
lst.append(lst[2], copy=False)

assert 3 == start_of_loop(lst)
