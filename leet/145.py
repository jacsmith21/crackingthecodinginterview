"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node({})'.format(self.val)


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        return [*self.postorderTraversal(root.left), *self.postorderTraversal(root.right), root.val]


# non recurse solutions
class SolutionV2:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        class Stack(deque):
            def push(self, item):
                self.append(item)

            def empty(self):
                return len(self) == 0

        if not root:
            return []

        node = root
        stack = Stack()
        postorder = []
        travelled = defaultdict(bool)
        while True:
            stack.push(node)

            if not travelled[node]:
                travelled[node] = True

            if node.left and not travelled[node.left]:
                node = node.left
                continue

            if node.right and not travelled[node.right]:
                node = node.right
                continue

            node = stack.pop()
            postorder.append(node.val)
            if stack.empty():
                break

            node = stack.pop()

        return postorder


tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
s = SolutionV2()
assert s.postorderTraversal(tree) == [1, 2, 3]

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
assert s.postorderTraversal(tree) == [3, 2, 1]
