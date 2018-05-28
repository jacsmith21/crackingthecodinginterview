"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        class TreeList:
            def __init__(self, lst):
                self._list = lst
                self.i = 0

            def insert_inorder(self, value):
                self._list[self.i] = value
                self.i += 1

            def export(self):
                return self._list

        tree_list = TreeList([0] * self.length(root))
        self.insert(root, tree_list)
        tree_list = tree_list.export()

        lo, hi = 0, len(tree_list)
        bounds = lo, hi
        while lo < (hi - 1):
            center = (lo + hi) // 2
            if target < tree_list[center]:
                hi = center
            else:
                lo = center
            bounds = lo, hi

        lo, hi = bounds
        index = 0
        closest = [0] * k
        while lo >= 0 and hi < len(tree_list) and index < k:
            if target - tree_list[lo] < tree_list[hi] - target:
                closest[index] = tree_list[lo]
                lo -= 1
            else:
                closest[index] = tree_list[hi]
                hi += 1

            index += 1

        # If we haven't filled our buffer that means we hit the end of the array somewheres. Fill it up using the opposite end.
        if index < k:
            if lo >= 0:
                while index < k:
                    closest[index] = tree_list[lo]
                    index += 1
                    lo -= 1
            else:
                while index < k:
                    closest[index] = tree_list[hi]
                    index += 1
                    hi += 1

        return closest

    def length(self, node):
        if node is None:
            return 0

        return 1 + self.length(node.left) + self.length(node.right)

    def insert(self, node, tree_list):
        if node is None:
            return

        self.insert(node.left, tree_list)
        tree_list.insert_inorder(node.val)
        self.insert(node.right, tree_list)


s = Solution()

tree = TreeNode(8)
tree.left = TreeNode(1)
assert s.closestKValues(tree, 6, 1) == [8]

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(5)
assert s.closestKValues(tree, 3.71212, 2) == [4, 3]
assert s.closestKValues(tree, 3712.12, 2) == [5, 4]
assert s.closestKValues(tree, 3712.12, 1) == [5]

