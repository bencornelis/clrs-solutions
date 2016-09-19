from linked_list import *

# Implement a stack using a singly linked list L. The operations PUSH and POP
# should still take O(1) time.

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        self.list.insert(item)

    def pop(self):
        item = self.list.head
        self.list.delete(item)
        return item
