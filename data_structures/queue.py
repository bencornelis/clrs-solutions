# Naive queue - enqueue is O(n), dequeue is O(1)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

# queue of at most n-1 elements using array of length n
# both enqueue and dequeue are run in O(1) time
class Que:
    def __init__(self, m):
        self.items = [None]*(m+1)
        self.end = m
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.head == self.tail + 1:
            raise Exception('The queue is full.')

        self.items[self.tail] = item
        if self.tail == self.end:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('The queue is empty.')

        x = self.items[self.head]
        if self.head == self.end:
            self.head = 0
        else:
            self.head += 1
        return x
