"""
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""

# If each needs to operate in O(1) time, we should store the data within each stack node. This information will contain the minimum element at the time the node was inserted.
