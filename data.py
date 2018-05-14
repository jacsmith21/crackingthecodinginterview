from structures import Tree


"""
      0
     /
    1
   / \
  2   3
 /\  / \
4  56   7
"""
tree = Tree.Node(0)
tree.l = Tree.Node(1)
tree.l.l = Tree.Node(2)
tree.l.l.l = Tree.Node(4)
tree.l.l.r = Tree.Node(5)
tree.l.r = Tree.Node(3)
tree.l.r.l = Tree.Node(5)
tree.l.r.r = Tree.Node(7)
