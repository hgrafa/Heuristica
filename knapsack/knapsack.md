- capacidade = disponibilidade
- valor_objeto = -tempo_de_processamento
- peso_objeto = tempo_de_processamento

complexidade = 2^n

```python
max_objetos = 1010
max_capacidade = 1010
dp = []

for _ in range(max_capacidade):
  vetor = []

  for _ in range(max_objetos):
    vetor.append(-1)

  matriz.append(vetor)

@cache
def melhor_mochila(aguenta, objetos, id_obj):

  # caso base
  if objeto_id == len(objetos):
    return 0

  if aguenta == 0:
    return 0

  # caso recursivo
  peso = objetos[id_obj].peso
  valor = objetos[id_obj].valor

  caso1 = melhor_mochila(aguenta, objetos, id + 1)
  caso2 = -1

  if aguenta - peso < 0:
    caso2 = valor + melhor_mochila(aguenta - peso, objetos, id + 1)

  return max(caso1, caso2)
```

```python
@cache
def knapsack_max_value1(weights, values, capacity):
    # Função recursiva para calcular o valor máximo da mochila
    if capacity == 0 or len(weights) == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade da mochila
    if weights[0] > capacity:  # validacoes de janela + de despobilidade
        # Item não cabe na mochila, passa para o próximo item
        return knapsack_max_value1(weights[1:], values[1:], capacity)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[0] + \
        knapsack_max_value1(weights[1:], values[1:], capacity - weights[0])
    excluded = knapsack_max_value1(weights[1:], values[1:], capacity)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)


@cache
def knapsack_max_value2(weights, values, capacity, index):
    # Função recursiva para calcular o valor máximo da mochila
    if index < 0 or capacity == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade da mochila
    if weights[index] > capacity:
        # Item não cabe na mochila, passa para o próximo item
        return knapsack_max_value2(weights, values, capacity, index - 1)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[index] + knapsack_max_value2(
        weights, values, capacity - weights[index], index - 1)
    excluded = knapsack_max_value2(weights, values, capacity, index - 1)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)


@cache
def knapsack_max_value3(weights, values, capacity, index, compartment_capacity):
    # Função recursiva para calcular o valor máximo da mochila compartimentada
    if index < 0 or capacity == 0 or compartment_capacity == 0:
        return 0

    # Verifica se o peso do item atual cabe na capacidade do compartimento atual
    if weights[index] > compartment_capacity:
        # Item não cabe no compartimento atual, passa para o próximo item
        return knapsack_max_value3(weights, values, capacity, index - 1, compartment_capacity)

    # Calcula o valor máximo considerando a inclusão e a exclusão do item atual
    included = values[index] + knapsack_max_value3(
        weights, values, capacity - weights[index], index - 1, compartment_capacity - weights[index])
    excluded = knapsack_max_value3(
        weights, values, capacity, index - 1, compartment_capacity)

    # Retorna o valor máximo entre a inclusão e a exclusão do item atual
    return max(included, excluded)
```
