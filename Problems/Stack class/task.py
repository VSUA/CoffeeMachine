class Stack():

    def __init__(self):
        self.array = []

    def push(self, el):
        self.array.append(el)

    def pop(self):
        last = self.array[len(self.array) - 1]
        self.array.pop(len(self.array) - 1)
        return last

    def peek(self):
        return self.array[len(self.array) - 1]

    def is_empty(self):
        if len(self.array) == 0:
            return True
        else:
            return False