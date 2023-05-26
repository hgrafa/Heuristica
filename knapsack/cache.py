from functools import cache

class KnapsackObject:
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


def get_compartiments(configs):
    compartiments = []

    for line in configs:
        obj_compartiments = []

        for i in range(len(line)):
            if line[i] == 1:
                obj_compartiments.append(i)

        compartiments.append(obj_compartiments)

    return compartiments


def get_objects(weights, values, compartiments):
    objects = []

    for pos in range(len(weights)):
        obj = KnapsackObject(weights[pos], values[pos], compartiments[pos])
        objects.append(obj)

    return objects


# Exemplo de uso
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
configs = [[1, 0, 1],
           [0, 1, 0],
           [1, 0, 1],
           [1, 1, 1]]

compartiments = get_compartiments(configs)
print(compartiments)

objects = get_objects(weights, values, compartiments)

partitions = 3
capacity = 7
