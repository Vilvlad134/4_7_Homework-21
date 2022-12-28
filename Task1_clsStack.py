class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return 'stack is empty'

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return 'stack is empty'

    def size(self):
        return len(self.stack)
