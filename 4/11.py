"""
You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
"""
import random

from structures import Tree


class RandomNode(Tree.Node):
    def __init__(self, key):
        super().__init__(key)
        self._count = None

    def get_random_node(self):
        if self.l is not None:
            l_weight = self.l.count
        else:
            l_weight = 0

        if self.r is not None:
            r_weight = self.r.count
        else:
            r_weight = 0

        choice = self.choose([self.l, self, self.r], [l_weight, 1, r_weight])
        if choice == self:
            return self
        else:
            return choice.get_random_node()

    @property
    def count(self):
        if self._count is None:
            self._count = 1
            self._count += self.l.count if self.l is not None else 0
            self._count += self.r.count if self.r is not None else 0

        return self._count

    @staticmethod
    def choose(choices, weights):
        total = 0
        for weight in weights:
            total += weight
        probabilities = [weight / total for weight in weights]

        number = random.random()
        total = 0
        for i, probability in enumerate(probabilities):
            total += probability
            if total > number:
                return choices[i]


tree = RandomNode(3)
tree.l = RandomNode(2)
tree.r = RandomNode(5)
tree.l.l = RandomNode(0)
tree.l.r = RandomNode(1)
tree.r.l = RandomNode(4)
tree.r.r = RandomNode(6)

print(tree.get_random_node().data)
