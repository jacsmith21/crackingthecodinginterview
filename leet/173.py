"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
import collections

from leet import TreeNode


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = collections.deque()
        self.current = None
        self.go_to_next(root)

    def go_to_next(self, node):
        if node is None:
            self.current = None
            return

        while node.left is not None:
            self.stack.append(node)
            node = node.left
        self.current = node

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current is not None

    def next(self):
        """
        :rtype: int
        """
        val = self.current.val
        if self.current.right is not None:
            self.go_to_next(self.current.right)
        elif not self.stack:
            self.current = None
        else:
            self.current = self.stack.pop()
        return val


def test():
    root = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())

    assert v == [1, 2, 3, 4, 5, 6, 7]
