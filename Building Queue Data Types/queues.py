from collections import deque
from heapq import heappop, heappush
from itertools import count

class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element) #Adding an element

    def dequeue(self):
        return self._elements.popleft() #Deleting an element

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue (IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count() #This will retain its current state in a tuple pushed onto the heap.
                                #If the elements has same priotity, then the earlier that was pushed gets the preccedence.

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1] #Used negative to properly access the last element
