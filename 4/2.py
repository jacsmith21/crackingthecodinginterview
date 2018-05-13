"""
Given a sorted (increasing order) array with unique integer elements, write an algo-
rithm to create a binary search tree with minimal height.
"""
from structures import Tree

nodes = [0, 1, 2, 3, 4, 5]
tree = Tree(*nodes)

assert tree == (0, 1, 2, 3, 4, 5)
