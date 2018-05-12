"""
Given a sorted (increasing order) array with unique integer elements, write an algo-
rithm to create a binary search tree with minimal height.
"""
from structures import Tree

nodes = [0, 1, 2, 3, 4, 5]
nodes = [Tree.Node(item) for item in nodes]

for i, node in enumerate(nodes):
    node.l, node.r = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None, nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None

tree = Tree()
tree.root = nodes[0]

assert tree == (0, 1, 2, 3, 4, 5)
