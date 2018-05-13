"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
"""
from structures import Tree, List

tree = Tree(1, 2, 3, 4, 5)


def get(node, depth, target):
    if depth == target:
        return List(node.data) if node is not None else None

    left = get(node.l, depth + 1, target)
    right = get(node.r, depth + 1, target)

    if left is not None:
        left.append(right)

    return left


assert [3] == get(tree.root, 0, target=0)
assert [2, 5] == get(tree.root, 0, target=1)
