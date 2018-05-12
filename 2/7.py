"""
Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth

node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""
from structures import List


# noinspection PyShadowingNames
def intersect(lst1, lst2):
    for n1 in lst1:
        for n2 in lst2:
            if n1 is n2:
                return n1

    return None


lst1 = List(1, 2, 3)

lst2 = List(1)
lst2.append(lst1[2], copy=False)

assert 3 == intersect(lst1, lst2)
