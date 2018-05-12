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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.data)


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
        if not isinstance(data, List.Node):
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
    class Node(BaseNode):
        pass

    def remove(self):
        if self.empty():
            raise EmptyException

        node = self.head
        self.head = self.head.next
        self.len -= 1
        return node

    def add(self, data):
        self.append(data)

    def empty(self):
        return self.head is None
