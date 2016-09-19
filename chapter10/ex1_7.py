# Naive implementation of stack with two queues
# Push is O(n), pop is O(n) (best and worst case)
class Stack:
    def __init__(self):
        self.cur_queue = Queue()
        self.next_queue = Queue()

    def push(self, item):
        self.cur_queue.enqueue(item)

    def pop(self):
        while True:
            item = self.cur_queue.dequeue()
            if self.cur_queue.is_empty():
                self.cur_queue, self.next_queue = self.next_queue, self.cur_queue
                return item
            self.next_queue.enqueue(item)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
