class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is already empty.')
        else:
            return self.items.pop()
