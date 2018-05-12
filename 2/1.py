"""
 Write code to remove duplicates from an unsorted linked list.
 How would you solve this problem if a temporary buffer is not allowed?
"""
import linkedlist
import structures

ll = structures.List(1, 2, 6, 3, 2)

unique = structures.List()

for node in ll:
    if node not in unique:
        unique.append(node)

assert unique == (1, 2, 6, 3)


