"""
Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree ofTi if there exists a node n in Ti such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""
from structures import Tree


def determine_height(node):
    if node is None:
        return 0
    else:
        return max(determine_height(node.l), determine_height(node.r)) + 1


# noinspection PyShadowingNames
def is_subtree(t1, t2, height=None):
    """
    This solution is not optimal. A better solution would be to start at every left leaf and to iterate up the tree at the same time. If something differs,
    then we just return False.
    """
    if t1 is None:
        return False

    if t1 == t2:
        return True

    return is_subtree(t1.l, t2, height) or is_subtree(t1.r, t2, height)


t1 = Tree.Node(0)
t1.l = Tree.Node(1)
t1.r = Tree.Node(2)
t1.l.l = Tree.Node(3)
t1.l.r = Tree.Node(4)
t1.r.l = Tree.Node(5)
t1.r.r = Tree.Node(6)

t2 = Tree.Node(6)
assert is_subtree(t1, t2)
assert is_subtree(t1, t1.l)
