"""
Implement a function to check if a linked list is a palindrome.
"""
from structures import List


# noinspection PyShadowingNames
def is_palindrome(lst):
    for n1, n2 in zip(lst, reversed(lst)):
        if n1 >= n2:
            break
        elif n1 != n2:
            return False

    return True


lst = List(1, 2, 3, 4, 3, 2, 1)
assert is_palindrome(lst)


lst = List(1, 2, 5, 2, 3)
assert not is_palindrome(lst)
