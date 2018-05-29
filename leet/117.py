"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Solution:
    @staticmethod
    def connect(root):
        while root:
            node = tem = TreeLinkNode(0)
            while root:
                if root.left:
                    node.next = node = root.left
                if root.right:
                    node.next = node = root.right
                root = root.next
            root = tem.next


class SolutionV2:
    def connect(self, root):
        self.recurse(root, 0, {})

    def recurse(self, node, level, rightmost):
        if node is None:
            return

        if level in rightmost:
            rightmost[level].next = node
            del rightmost[level]

        self.recurse(node.left, level + 1, rightmost)
        self.recurse(node.right, level + 1, rightmost)

        rightmost[level] = node


def test(s):
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right = TreeLinkNode(3)
    root.right.right = TreeLinkNode(7)
    s.connect(root)

    assert root.left.next == root.right
    assert root.right.next is None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
