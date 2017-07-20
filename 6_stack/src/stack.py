class Stack(object):
    def __init__(self):
        self._stack = []

    def get_size(self):
        return len(self._stack)

    def push(self, input):
        return self._stack.append(input)

    def pop(self):
        return None if len(self._stack) == 0 else self._stack.pop()
