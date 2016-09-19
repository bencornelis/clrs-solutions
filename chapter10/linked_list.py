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
        self.head = x

    def delete(self, x):
        if x == self.head:
            self.head = self.head.next
        else:
            y = self.head
            while y is not None and y.next != x:
                y = y.next
            if y is None:
                return None
            y.next = x.next

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
