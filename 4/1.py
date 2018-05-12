"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
from structures import Graph, Queue

g = Graph()
g.add(0, 4)
g.add(1, 4)
g.add(2, 5)
g.add(3, 5)
g.add(4, 6)
g.add(5, 6)
g.add(6, 7)
g.add(7, 8)
g.add(8, 9)
g.add(8, 10)
g.add(9, 11)
g.add(9, 12)
g.add(10, 13)
g.add(10, 14)


def path_exists(g, start, target):
    start = g[start]

    queue = Queue()
    for child in start:
        queue.enqueue(child)

    for child in queue:
        if child.seen:
            return

        if child == target:
            return True
        else:
            child.seen = True
            for child_of_child in child:
                queue.enqueue(child_of_child)
    else:
        return False


assert path_exists(g, 0, 14)
assert not path_exists(g, 0, 3)
