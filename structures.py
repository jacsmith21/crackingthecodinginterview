class EmptyException(Exception):
    pass


class BaseNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def __gt__(self, other):
        if isinstance(other, BaseNode):
            other = other.data

        return self.data > other

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Node({})'.format(str(self.data))


class List:
    class Node(BaseNode):
        def __init__(self, data):
            super().__init__(data)
            self.prev = None

    def __init__(self, *nums, reverse=False):
        self.head = None
        self.tail = None
        self.len = 0

        if reverse:
            for n in reversed(nums):
                self.append(n)
        else:
            for n in nums:
                self.append(n)

    def append(self, data, copy=True):
        if isinstance(data, List):
            self.append(data.head)
            return
        elif not isinstance(data, BaseNode):
            if not copy:
                raise ValueError('data is not Node, but copy is set to False')

            end = List.Node(data)
        else:
            if copy is True:
                end = List.Node(data.data)
            else:
                end = data

        if self.head is None:
            self.head = end
            self.tail = end
        else:
            self.tail.next = end
            end.prev = self.tail
            self.tail = end

        self.len += 1

    def get_and_remove(self, index):
        for i, n in enumerate(self):
            if i == index:
                if n.prev is None:
                    self.head = n.next
                else:
                    n.prev.next = n.next
                if n.next is None:
                    self.tail = n.prev
                else:
                    n.next.prev = n.prev
                return n
        return None

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

    def __len__(self):
        return self.len

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


class Stack(List):
    class Node(BaseNode):
        pass

    def __init__(self, *nums):
        super().__init__(*nums, reverse=True)

    def pop(self):
        if self.empty():
            raise EmptyException

        data = self.tail.data
        prev = self.tail.prev
        if prev is not None:
            prev.next = None
        else:
            self.head = None

        self.tail = prev

        self.len -= 1
        return data

    def push(self, data):
        self.append(data)

    def peek(self):
        return self.tail.data

    def empty(self):
        return self.tail is None


class Queue(List):
    def enqueue(self, item):
        self.append(item, copy=False)

    def dequeue(self):
        return self.get_and_remove(0)


class Graph:
    class Node(BaseNode):
        def __init__(self, key):
            super().__init__(key)
            self.children = []
            self.seen = False

        def __iter__(self):
            return iter(self.children)

    def __init__(self, *nodes):
        self.nodes = {}
        for node in nodes:
            self.nodes[node.data] = node

    def add(self, a, b):
        a = self[a]
        b = self[b]

        a.children.append(b)

    def __getitem__(self, key):
        if isinstance(key, Graph.Node):
            return key

        if key not in self.nodes:
            self.nodes[key] = Graph.Node(key)

        return self.nodes[key]


class Tree:
    class Node(BaseNode):
        def __init__(self, key):
            super().__init__(key)
            self._l = None
            self._r = None
            self.parent = None

        @property
        def l(self):
            return self._l

        @l.setter
        def l(self, l):
            self._l = l
            self._l.parent = self

        @property
        def r(self):
            return self._r

        @r.setter
        def r(self, r):
            self._r = r
            self._r.parent = self

        def __iter__(self):
            if self.l is not None:
                for v in self.l:
                    yield v
            yield self.data
            if self.r is not None:
                for v in self.r:
                    yield v

        def __str__(self):
            return ', '.join([str(n) for n in self])

        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
            if self.l is None and self.r is None:
                return self.data == other

            for this, that in zip(self, other):
                if this != that:
                    return False
            else:
                return True

    def __init__(self, *nums):
        nodes = [Tree.Node(item) for item in nums]
        self.root = None
        self.root = self.initiate(nodes)

    def initiate(self, nums):
        if len(nums) == 0:
            return None

        index = int(len(nums) / 2)
        middle = nums[index]
        middle = Tree.Node(middle)
        middle.l = self.initiate(nums[:index])
        middle.r = self.initiate(nums[(index + 1):])

        return middle

    def __iter__(self):
        return iter(self.root)

    def __str__(self):
        return self.root.__str__() if self.root is not None else 'Empty Tree'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.root.__eq__(other)
