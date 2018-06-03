"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""


class Solution:
    # noinspection PyPep8Naming
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        i_child = None
        parent1 = None
        parent2 = None

        relationships = {}
        for edge in edges:
            parent = edge[0] - 1
            child = edge[1] - 1

            if child == 0:
                return edge

            if child in relationships:
                i_child = child
                parent1 = relationships[child]
                parent2 = parent
            else:
                relationships[child] = parent

        if self.in_path(parent1, i_child, relationships):
            return [parent1 + 1, i_child + 1]
        else:
            return [parent2 + 1, i_child + 1]

    def in_path(self, source, target, edges):
        if source == target:
            return True
        else:
            if source in edges:
                return self.in_path(edges[source], target, edges)
            else:
                return False


assert Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert Solution().findRedundantDirectedConnection([[1, 2], [1, 4], [2, 3], [4, 3]]) == [4, 3]
assert Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
assert Solution().findRedundantDirectedConnection([[4, 2], [1, 5], [5, 2], [5, 3], [2, 4]]) == [4, 2]
