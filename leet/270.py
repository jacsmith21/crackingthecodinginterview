"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if target > root.val and root.right is not None:
            value = self.closestValue(root.right, target)
        elif target < root.val and root.left is not None:
            value = self.closestValue(root.left, target)
        else:
            return root.val

        if abs(value - target) > abs(root.val - target):
            return root.val
        else:
            return value


def test(s):
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(5)
    s.closestValue(root, 3.71428) == 4
