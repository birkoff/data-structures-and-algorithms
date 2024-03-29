
class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)