class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        node = Stack.Node(data)
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top.data

    def empty(self):
        return self.top is None


class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def remove(self):
        node = self.first
        self.first = self.first.next
        return node

    def push(self, data):
        node = Queue.Node(data)
        self.last.next = node
        self.first = node

    def peek(self):
        return self.first.data

    def empty(self):
        return self.first is None


class List:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __eq__(self, other):
            if isinstance(other, List.Node):
                return self.data == other.data
            else:
                return self.data == other

        def __lt__(self, other):
            if isinstance(other, List.Node):
                other = other.data

            return self.data < other

        def __ge__(self, other):
            if isinstance(other, List.Node):
                other = other.data

            return self.data >= other

        def __repr__(self):
            return self.__str__()

        def __str__(self):
            return str(self.data)

    def __init__(self, *nums):
        self.head = None
        self.tail = None
        for n in nums:
            self.append(n)

    def append(self, data):
        if not isinstance(data, List.Node):
            end = List.Node(data)
        else:
            end = List.Node(data.data)

        if self.head is None:
            self.head = end
            self.tail = end
        else:
            self.tail.next = end
            end.prev = self.tail
            self.tail = end

    def __contains__(self, node):
        for n in self:
            if n.data == node.data:
                return True
        else:
            return False

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    def __reversed__(self):
        n = self.tail
        while n is not None:
            yield n
            n = n.prev

    def __eq__(self, other):
        for this, that in zip(self, other):
            if this != that:
                return False
        else:
            return True

    def __getitem__(self, index):
        for i, n in enumerate(self):
            if i == index:
                return n
        else:
            return None

    @staticmethod
    def remove(node):
        n = node
        while n.next is not None:
            n.data = n.next.data
            n = n.next

    def partition(self, value):
        tail = self.tail

        n = self.head
        prev = None
        while n is not tail:
            if n >= value:
                if prev is None:
                    self.head = n.next
                else:
                    prev.next = n.next

                self.append(n)

                n = prev.next
            else:
                prev = n
                n = n.next

    def __add__(self, other):
        num1 = 0
        i = 1
        for n in self:
            num1 += i * n.data
            i *= 10

        num2 = 0
        i = 1
        for n in other:
            num2 += i * n.data
            i *= 10

        return num1 + num2

    def __str__(self):
        return ', '.join([str(n) for n in self])

    def __repr__(self):
        return self.__str__()
