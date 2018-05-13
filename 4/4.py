"""
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
from structures import Tree


def balanced(node):
    if node is None:
        return True, 0

    is_balanced, left = balanced(node.l)
    if not is_balanced:
        return False, None

    is_balanced, right = balanced(node.r)
    if not is_balanced:
        return False, None

    if abs(left - right) > 1:
        return False, None

    return True, max(left, right) + 1


tree = Tree.Node(0)
tree.l = Tree.Node(1)
tree.r = Tree.Node(1)
tree.l.l = Tree.Node(2)
tree.l.r = Tree.Node(2)
assert balanced(tree)[0]

tree = Tree.Node(0)
tree.l = Tree.Node(1)
tree.l.l = Tree.Node(2)
assert not balanced(tree)[0]
assert not balanced(tree)[0]
