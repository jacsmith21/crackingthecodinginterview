"""
Implement a function to check if a binary tree is a binary search tree.
"""
from structures import Tree


# TODO: Fix this algorithm
def binary_tree(node):
    if node is None:
        return True

    if node.l is not None and node.l > node:
        return False
    elif not binary_tree(node.l):
        return False

    if node.r is not None and node.r < node:
        return False
    elif not binary_tree(node.r):
        return False

    return True,


tree = Tree.Node(1)
tree.l = Tree.Node(-1)
tree.l.l = Tree.Node(-2)
tree.l.r = Tree.Node(0)
tree.r = Tree.Node(2)
assert binary_tree(tree)

tree = Tree.Node(0)
tree.l = Tree.Node(1)
tree.r = Tree.Node(2)
assert not binary_tree(tree)
