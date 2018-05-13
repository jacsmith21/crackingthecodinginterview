"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""
from structures import Tree


def next_node(node):
    if node.l is not None:
        return node.l
    elif node.r is not None:
        return node.r
    else:
        return node.parent


tree = Tree.Node(0)
tree.l = Tree.Node(-2)
tree.l.l = Tree.Node(-3)
tree.l.r = Tree.Node(-1)
assert next_node(tree) is None
assert next_node(tree.l) is tree
assert next_node(tree.l.r) is tree.l

