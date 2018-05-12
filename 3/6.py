"""
An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked List data structure.
"""
from structures import List


class Dog(List.Node):
    pass


class Cat(List.Node):
    pass


class PetQueue(List):
    def dequeue_dog(self):
        return self.dequeue_types([Dog])

    def dequeue(self, n):
        if n.prev is not None:
            n.prev.next = n.next
        else:
            self.head = n.next

        if n.next is not None:
            n.next.prev = n.prev
        else:
            self.tail = n.prev

    def dequeue_cat(self):
        return self.dequeue_types([Cat])

    def dequeue_any(self):
        return self.dequeue_types([Dog, Cat])

    def dequeue_types(self, types):
        for n in self:
            for t in types:
                if isinstance(n, t):
                    self.dequeue(n)
                    return n
        else:
            return None

    def enqueue(self, data):
        self.append(data, copy=False)


queue = PetQueue()
queue.enqueue(Dog('dog1'))
queue.enqueue(Cat('cat1'))
queue.enqueue(Dog('dog2'))
queue.enqueue(Cat('cat2'))
queue.enqueue(Cat('cat3'))

assert 'cat1' == queue.dequeue_cat()
assert 'dog1' == queue.dequeue_dog()
assert 'dog2' == queue.dequeue_any()
