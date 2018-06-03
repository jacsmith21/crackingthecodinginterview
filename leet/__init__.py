class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        node = self
        for val in other:
            if node is None or val != node.val:
                return False
            else:
                node = node.next
        return True


def make(nums):
    start = ListNode(nums[0])
    node = start
    for n in nums[1:]:
        node.next = ListNode(n)
        node = node.next
    return start


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def from_list(nums):
        if len(nums) == 0:
            return None

        index = int(len(nums) / 2)
        middle = nums[index]
        middle = TreeNode(middle)
        middle.left = TreeNode.from_list(nums[:index])
        middle.right = TreeNode.from_list(nums[(index + 1):])

        return middle

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def make_tree(nums):
    return TreeNode.from_list(nums)
