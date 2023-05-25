from functools import cache


def foo(a, b):
    return a*a + b/2


@cache
def cached_foo(a, b):
    return a*a + b/2


print(
    foo(2, 2), foo(4, 4),
    foo(2, 2), foo(4, 4)
)

print(
    cached_foo(2, 2), cached_foo(4, 4),
    cached_foo(2, 2), cached_foo(4, 4)
)


@cache
def knapsack_max_value(weights, values, capacity):
    # Função recursiva para calcular o valor máximo da mochila
    if capacity == 0 or len(weights) == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade da mochila
    if weights[0] > capacity:  # validacoes de janela + de despobilidade
        # Item não cabe na mochila, passa para o próximo item
        return knapsack_max_value(weights[1:], values[1:], capacity)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[0] + \
        knapsack_max_value(weights[1:], values[1:], capacity - weights[0])
    excluded = knapsack_max_value(weights[1:], values[1:], capacity)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)


@cache
def knapsack_max_value(weights, values, capacity, index):
    # Função recursiva para calcular o valor máximo da mochila
    if index < 0 or capacity == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade da mochila
    if weights[index] > capacity:
        # Item não cabe na mochila, passa para o próximo item
        return knapsack_max_value(weights, values, capacity, index - 1)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[index] + knapsack_max_value(
        weights, values, capacity - weights[index], index - 1)
    excluded = knapsack_max_value(weights, values, capacity, index - 1)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)


@cache
def knapsack_max_value(weights, values, capacity, index, compartment_capacity):
    # Função recursiva para calcular o valor máximo da mochila compartimentada
    if index < 0 or capacity == 0 or compartment_capacity == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade do compartimento atual
    if weights[index] > compartment_capacity:
        # Item não cabe no compartimento atual, passa para o próximo item
        return knapsack_max_value(weights, values, capacity, index - 1, compartment_capacity)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[index] + knapsack_max_value(
        weights, values, capacity - weights[index], index - 1, compartment_capacity - weights[index])
    excluded = knapsack_max_value(
        weights, values, capacity, index - 1, compartment_capacity)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)


# Exemplo de uso
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
