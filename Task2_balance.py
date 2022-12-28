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


def balance_string(string_bracket):
    equality = {'(': ')',
                '[': ']',
                '{': '}'}
    open_bracket = ('(', '[', '{')
    close_bracket = (')', ']', '}')
    balance = Stack()
    for elem in list(string_bracket):
        if elem in open_bracket:
            balance.push(elem)
        elif elem in close_bracket and balance.is_empty() is False:
            return 'Несбалансированно'
        elif elem in close_bracket and equality[balance.peek()] == elem:
            balance.pop()
        else:
            return 'Несбалансированно'

    if balance.is_empty() is False:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(balance_string('[{(())}]'))
