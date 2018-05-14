"""
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""
from structures import Tree


def next_smallest(node):
    if node.l is not None:
        return next_smallest(node.l)
    else:
        return node


def next_node(node):
    if node.r is not None:
        return next_smallest(node.r)
    elif node.parent is not None:
        return node.parent
    else:
        return None


"""
      0
     /
   -2
  /  \
-3    -1
      /
    -1.5
"""
tree = Tree.Node(0)
tree.l = Tree.Node(-2)
tree.l.l = Tree.Node(-3)
tree.l.r = Tree.Node(-1)
tree.l.r.l = Tree.Node(-1.5)

assert next_node(tree) is None
assert next_node(tree.l) is tree.l.r.l
assert next_node(tree.l.l) is tree.l

