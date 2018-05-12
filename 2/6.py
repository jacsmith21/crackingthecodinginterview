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


def recurse(node1, node2):
    if node2 is None:  # the list is even
        return True, None

    if node2.next is None:  # the list is odd
        return True, node1.next

    palindrome, counterpart = recurse(node1.next, node2.next.next)

    if not palindrome:
        return False, None

    if counterpart is None:
        counterpart = node2

    if node1 != counterpart:
        return False, None

    return True, counterpart.next


def is_palindrome_v2(ll):
    palindrome, _ = recurse(ll.head, ll.head)
    return palindrome


ll = List(1, 2, 2, 1)
assert is_palindrome_v2(ll)
assert is_palindrome(ll)


lst = List(1, 2, 3, 4, 3, 2, 1)
assert is_palindrome(lst)
assert is_palindrome_v2(lst)


lst = List(1, 2, 5, 2, 3)
assert not is_palindrome(lst)
assert not is_palindrome_v2(lst)
