"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
from collections import defaultdict, OrderedDict


class SolutionV2:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        class Node:
            def __init__(self, name):
                self.name = name
                self.children = {}

            def append(self, node):
                self.children[node] = False

            def __iter__(self):
                return iter(self.children)

            def travelled(self, node):
                return self.children[node]

            def travel(self, node):
                self.children[node] = True

            def __repr__(self):
                return 'Node({})'.format(self.name)

            def __str__(self):
                return self.__repr__()

        nodes = {}
        for ticket in tickets:
            src = ticket[0]
            dst = ticket[1]
            if src not in nodes:
                nodes[src] = Node(src)
            if dst not in nodes:
                nodes[dst] = Node(dst)

            nodes[src].append(nodes[dst])

        node = nodes['JFK']
        return self.recurse(node)

    def recurse(self, node):
        smallest = None
        while True:
            for child in node:
                if node.travelled(child):
                    continue

                if smallest is None:
                    smallest = child
                else:
                    smallest = child if child.name < smallest.name else smallest

            if smallest is None:
                return 1, [node.name]
            else:
                node.travel(smallest)
                return [node.name, *self.recurse(smallest)]


class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        class Graph:
            def __init__(self):
                self.graph = defaultdict(OrderedDict)

            def append(self, src, dst):
                self.graph[src][dst] = False

            def __getitem__(self, item):
                return self.graph[item]

            def travel(self, src, dst):
                self.graph[src][dst] = True

            def travelled(self, src, dst):
                return self.graph[src][dst]

        graph = Graph()
        for ticket in tickets:
            graph.append(*ticket)

        return self.recurse('JFK', graph)

    def recurse(self, src, graph):
        order = []
        for dst in sorted(graph[src]):
            if graph.travelled(src, dst):
                continue
            else:
                graph.travel(src, dst)
                order = [*self.recurse(dst, graph), *order]
        return [src, *order]


s = Solution()
assert s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
assert s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]) == ["JFK", "NRT", "JFK", "KUL"]
assert s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
