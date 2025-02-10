class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def next(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
