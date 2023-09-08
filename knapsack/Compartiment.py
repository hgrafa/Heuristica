# Arvores - CRUD

class Compartiment:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def maxed_out(self):
        total = 0
        for item in self.items:
            total += item.value

        return total > self.capacity

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)
