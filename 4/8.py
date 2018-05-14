"""
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""

# Option 1: Recurse of the tree from one node and mark all of the nodes as `seen`
# then recurse up from the second node and return the first node that is marked as `seen`

# Option 2: Recurse up both of the nodes at the same time until you hit the root node of each. When both of the roots have been hit,
# recurse back and return the previous  THis option would be much more space intensive but a cleaner solution.

# For both of these solutions, it may be useful to move and check at the same time to improve the best cast scenario.
import data
from structures import Tree


class SeenNode(Tree.Node):
    def __init__(self, key):
        super().__init__(key)
        self.seen = False


def recurse_and_mark(node):
    if node is None:
        return

    node.seen = True
    recurse_and_mark(node.parent)


def common(n1, n2):
    recurse_and_mark(n1)

    node = n2
    while not node.seen:
        node = node.parent

    return node


def reset(node):
    if node is None:
        return

    node.seen = False

    reset(node.l)
    reset(node.r)


tree = data.tree
assert 3 == common(tree.l.r.l, tree.l.r.r)

reset(tree)
assert 1 == common(tree.l.l.l, tree.l.r.r)
