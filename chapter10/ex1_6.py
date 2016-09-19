from stack import *

# Implements a queue with two stacks
# Enqueue runs in O(1), dequeue in O(n)
class Queue:
    def __init__(self):
        self.en_stack = Stack()
        self.de_stack = Stack()

    def enqueue(self, item):
        self.en_stack.push(item)

    def dequeue(self):
        if self.de_stack.is_empty():
            while not self.en_stack.is_empty():
                item = self.en_stack.pop()
                self.de_stack.push(item)

        return self.de_stack.pop()
