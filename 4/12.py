"""
You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""
import data


def start_path(node, sum_so_far, target):
    if node is None:
        return 0

    sum_so_far += node.data

    if sum_so_far == target:
        return 1
    elif sum_so_far > target:
        return 0
    else:
        return start_path(node.l, sum_so_far, target) + start_path(node.r, sum_so_far, target)


def start(root, target):
    if root is None:
        return 0

    total = start_path(root, sum_so_far=0, target=target)
    total += start(root.l, target)
    total += start(root.r, target)

    return total


assert 4 == start(data.tree, target=7)
