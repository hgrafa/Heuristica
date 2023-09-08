from functools import cache


class Item:
    def __init__(self, weight, value, available_compartiments):
        self.weight = weight
        self.value = value
        self.available_compartiments = available_compartiments

    def __str__(self):
        aux = '------------\n'
        aux += f'Peso: {self.weight}, Valor: {self.value}\n'
        aux += f'Compartimentos aceitos: {self.available_compartiments}\n'
        aux += '------------'
        return aux


class Knapsack:
    def __init__(self, capacities):
        self.partitions = len(capacities)
        self.capacities = capacities
        self.arrangement = [self.partitions * []]

    def maxed_out(self):
        for capacity in self.capacities:
            if capacity > 0:
                return False

        return True

    def evaluate(self):
        total = 0
        for arrange in self.arrangements:
            total += sum(arrange)
        return total

    def copy(self):
        return Knapsack(self.capacities)

    def append(self, partition, object):
        self.arrangement[partition].append(object)

    def remove(self, partition, object):
        self.arrangement[partition].remove(object)


def get_compartiments(configs):
    compartiments = []

    for line in configs:
        obj_compartiments = []

        for i in range(len(line)):
            if line[i] == 1:
                obj_compartiments.append(i)

        compartiments.append(obj_compartiments)

    return compartiments


def get_items(weights, values, compartiments):
    items = []

    for pos in range(len(weights)):
        obj = Item(weights[pos], values[pos], compartiments[pos])
        items.append(obj)

    return items


@cache
def knapsack_solver(knapsack, objects, id=0):

    # caso base: acabaram os objetos
    if id == len(objects):
        return 0

    # caso base: maximizei a mochila
    if knapsack.maxed_out():
        return 0

    cases = []
    cases.append(knapsack_solver(knapsack.copy(), objects, id+1))

    for compartment in objects[id].available_compartiments:
        sub_knapsack = knapsack.copy()
        sub_knapsack.add(compartment, objects[id])
        cases.append(knapsack_solver(sub_knapsack, objects, id+1))

    max_value = -1
    for case in cases:
        value = case.evaluate()
        if value > max_value:
            max_value = value

    return max_value


weights = [4, 3, 6, 2]
values = [9, 7, 12, 4]
capacities = [10, 2, 3]
configs = [[1, 0, 0],
           [1, 0, 0],
           [1, 0, 0],
           [1, 0, 0]]

compartiments = get_compartiments(configs)
items = get_items(weights, values, compartiments)
knapsack = Knapsack(capacities)

knapsack_solver(knapsack, items)
