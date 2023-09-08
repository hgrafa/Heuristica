from Item import Item
from functools import cache


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
        item = Item(weights[pos], values[pos], compartiments[pos])
        items.append(item)
    return items


def has_maxed_out(capacities):
    return sum(capacities) == 0

# TODO
# def addItemTo(compartiment_id, item):
#     com

# def removeItemFrom(compartiment_id, item):


@cache
def knapsack_solver(capacities, items, id=0):
    if id == len(items) or has_maxed_out(capacities):
        return 0

    possibilities = []
    item = items[id]
    for compartiment_id in item.available_compartiments:
        copy = list(capacities)
        copy[compartiment_id] -= item.weight
        possibility = item.value
        possibility += knapsack_solver(tuple(copy), items, id+1)
        possibilities.append(possibility)

    best = -1

    for possibility in possibilities:
        if possibility > best:
            best = possibility

    return best


weights = [4, 3, 6]
values = [9, 7, 12]
capacities = [10, 5, 15]
configs = [[1, 0, 0],
           [0, 1, 0],
           [0, 1, 1]]

compartiments = get_compartiments(configs)
items = get_items(weights, values, compartiments)
result = knapsack_solver(tuple(capacities), tuple(items))
print(result)

# -------------------------

# key = (id, tuple(knapsack.capacities))
# if key in cache:
#     return cache[key]

# cases = []
# cases.append(knapsack_solver(knapsack.copy(), objects, id + 1, cache))

# for compartment in objects[id].available_compartiments:
#     sub_knapsack = knapsack.copy()
#     sub_knapsack.append(compartment, objects[id])
#     cases.append(knapsack_solver(sub_knapsack, objects, id + 1, cache))

# max_value = -1
# max_knapsack = None
# for case in cases:
#     if case.evaluate() > max_value:
#         max_value = case.evaluate()
#         max_knapsack = case

# cache[key] = max_knapsack

# return max_knapsack
