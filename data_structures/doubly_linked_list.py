# Doubly Linked list
# Search is O(n), Insert and Delete are O(1)
class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

        if x.next is not None:
            x.next.prev = x.prev


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
