class Knapsack:
    def __init__(self, capacities):
        self.partitions = len(capacities)
        self.capacities = capacities
        self.arrangement = [[] for _ in range(self.partitions)]

    def maxed_out(self):
        for capacity in self.capacities:
            if capacity > 0:
                return False
        return True

    def evaluate(self):
        total = 0
        for arrange in self.arrangement:
            for item in arrange:
                total += item.value

        return total

    def copy(self):
        return Knapsack(self.capacities)

    def append(self, partition, obj):
        self.arrangement[partition].append(obj)

    def remove(self, partition, obj):
        self.arrangement[partition].remove(obj)

    def __str__(self):
        aux = f'Total = {self.evaluate()}\n'
        for arrange in self.arrangement:
            for item in arrange:
                aux += f'{item}, '
            aux += '\n'
        return aux
