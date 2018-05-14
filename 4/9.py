"""
A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
"""
import data


def weave(l1, l2, prefix=None):
    prefix = prefix or []
    combinations = []
    if not l1:
        return [prefix + l2]
    elif not l2:
        return [prefix + l1]

    combinations.extend(weave(l1[1:], l2, [*prefix, l1[0]]))
    combinations.extend(weave(l1, l2[1:], [*prefix, l2[0]]))

    return combinations


assert [[0, 1, 2, 3], [0, 2, 1, 3], [0, 2, 3, 1],
        [2, 0, 1, 3], [2, 0, 3, 1], [2, 3, 0, 1]] == weave([0, 1], [2, 3])
assert [[0, 1], [1, 0]] == weave([0], [1])


def tree_combinations(node):
    if node is None:
        return []

    l_combinations = tree_combinations(node.l)
    r_combinations = tree_combinations(node.r)

    if not l_combinations and not r_combinations:
        combinations = [[]]
    elif not l_combinations:
        combinations = r_combinations
    elif not r_combinations:
        combinations = l_combinations
    else:
        combinations = []
        for l_combination in l_combinations:
            for r_combination in r_combinations:
                combinations.extend(weave(l_combination, r_combination))

    for combination in combinations:
        combination.insert(0, node.data)

    return combinations


assert [[4]] == tree_combinations(data.tree.l.l.l)
assert [[2, 4, 5], [2, 5, 4]] == tree_combinations(data.tree.l.l)

assert tree_combinations(data.tree.l) == \
                                    [[1, 2, 4, 5, 3, 5, 7], [1, 2, 4, 3, 5, 5, 7], [1, 2, 4, 3, 5, 5, 7], [1, 2, 4, 3, 5, 7, 5], [1, 2, 3, 4, 5, 5, 7],
                                     [1, 2, 3, 4, 5, 5, 7], [1, 2, 3, 4, 5, 7, 5], [1, 2, 3, 5, 4, 5, 7], [1, 2, 3, 5, 4, 7, 5], [1, 2, 3, 5, 7, 4, 5],
                                     [1, 3, 2, 4, 5, 5, 7], [1, 3, 2, 4, 5, 5, 7], [1, 3, 2, 4, 5, 7, 5], [1, 3, 2, 5, 4, 5, 7], [1, 3, 2, 5, 4, 7, 5],
                                     [1, 3, 2, 5, 7, 4, 5], [1, 3, 5, 2, 4, 5, 7], [1, 3, 5, 2, 4, 7, 5], [1, 3, 5, 2, 7, 4, 5], [1, 3, 5, 7, 2, 4, 5],
                                     [1, 2, 4, 5, 3, 7, 5], [1, 2, 4, 3, 5, 7, 5], [1, 2, 4, 3, 7, 5, 5], [1, 2, 4, 3, 7, 5, 5], [1, 2, 3, 4, 5, 7, 5],
                                     [1, 2, 3, 4, 7, 5, 5], [1, 2, 3, 4, 7, 5, 5], [1, 2, 3, 7, 4, 5, 5], [1, 2, 3, 7, 4, 5, 5], [1, 2, 3, 7, 5, 4, 5],
                                     [1, 3, 2, 4, 5, 7, 5], [1, 3, 2, 4, 7, 5, 5], [1, 3, 2, 4, 7, 5, 5], [1, 3, 2, 7, 4, 5, 5], [1, 3, 2, 7, 4, 5, 5],
                                     [1, 3, 2, 7, 5, 4, 5], [1, 3, 7, 2, 4, 5, 5], [1, 3, 7, 2, 4, 5, 5], [1, 3, 7, 2, 5, 4, 5], [1, 3, 7, 5, 2, 4, 5],
                                     [1, 2, 5, 4, 3, 5, 7], [1, 2, 5, 3, 4, 5, 7], [1, 2, 5, 3, 5, 4, 7], [1, 2, 5, 3, 5, 7, 4], [1, 2, 3, 5, 4, 5, 7],
                                     [1, 2, 3, 5, 5, 4, 7], [1, 2, 3, 5, 5, 7, 4], [1, 2, 3, 5, 5, 4, 7], [1, 2, 3, 5, 5, 7, 4], [1, 2, 3, 5, 7, 5, 4],
                                     [1, 3, 2, 5, 4, 5, 7], [1, 3, 2, 5, 5, 4, 7], [1, 3, 2, 5, 5, 7, 4], [1, 3, 2, 5, 5, 4, 7], [1, 3, 2, 5, 5, 7, 4],
                                     [1, 3, 2, 5, 7, 5, 4], [1, 3, 5, 2, 5, 4, 7], [1, 3, 5, 2, 5, 7, 4], [1, 3, 5, 2, 7, 5, 4], [1, 3, 5, 7, 2, 5, 4],
                                     [1, 2, 5, 4, 3, 7, 5], [1, 2, 5, 3, 4, 7, 5], [1, 2, 5, 3, 7, 4, 5], [1, 2, 5, 3, 7, 5, 4], [1, 2, 3, 5, 4, 7, 5],
                                     [1, 2, 3, 5, 7, 4, 5], [1, 2, 3, 5, 7, 5, 4], [1, 2, 3, 7, 5, 4, 5], [1, 2, 3, 7, 5, 5, 4], [1, 2, 3, 7, 5, 5, 4],
                                     [1, 3, 2, 5, 4, 7, 5], [1, 3, 2, 5, 7, 4, 5], [1, 3, 2, 5, 7, 5, 4], [1, 3, 2, 7, 5, 4, 5], [1, 3, 2, 7, 5, 5, 4],
                                     [1, 3, 2, 7, 5, 5, 4], [1, 3, 7, 2, 5, 4, 5], [1, 3, 7, 2, 5, 5, 4], [1, 3, 7, 2, 5, 5, 4], [1, 3, 7, 5, 2, 5, 4]]
