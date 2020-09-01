class Stack():

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        if not len(self.stack):
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
