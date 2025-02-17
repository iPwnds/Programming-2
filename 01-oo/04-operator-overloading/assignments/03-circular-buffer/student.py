class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def __len__(self):
        return len(self.buffer)

    def add(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer.pop(0)
            self.buffer.append(item)

    def __getitem__(self, index):
        if 0 <= index < len(self.buffer):
            return self.buffer[index]
        raise IndexError("Index out of range")
