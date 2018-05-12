class Node:
    def __init__(self, data):
        self.data = data

    def append(self, data):
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next

        n.next = end
