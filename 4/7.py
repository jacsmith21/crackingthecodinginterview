"""
You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.

EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""
from structures import Graph


class ProjectNode(Graph.Node):
    def __init__(self, key):
        super().__init__(key)
        self.built = False


# noinspection PyShadowingNames
def build(project):
    if project.built:
        return []
    elif project.seen and not project.built:
        raise BlockingIOError  # a random error tbh
    else:
        project.seen = True
        order = []
        for child in project.children:
            order.extend(build(child))
        project.built = True

    return [*order, project]


# noinspection PyShadowingNames
def determine_order(projects):
    order = []
    for project in projects:
        order.extend(build(project))
    return order


projects = 'a', 'b', 'c', 'd', 'e', 'f'
projects = [ProjectNode(project) for project in projects]
graph = Graph(*projects)

dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
for dependency, project in dependencies:
    graph.add(project, dependency)


assert ['f', 'a', 'b', 'd', 'c', 'e'] == determine_order(projects)
