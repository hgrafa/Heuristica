import random

# Definindo os dados do problema

objetos = [
    {"peso": 2, "valor": 10, "categoria": 3},
    {"peso": 4, "valor": 8, "categoria": 4},
    {"peso": 6, "valor": 12, "categoria": 5},
    {"peso": 3, "valor": 6, "categoria": 4},
    {"peso": 5, "valor": 9, "categoria": 3},
]

capacidade_bolso = 20
categorias_aceitas = [3, 4, 5]

# Parâmetros do Simulated Annealing
temperatura_inicial = 1000
fator_resfriamento = 0.95
numero_iteracoes = 1000

# Função para calcular o valor de uma solução


def calcular_valor(sol):
    valor_total = 0
    for i in range(len(sol)):
        if sol[i] == 1:
            valor_total += objetos[i]["valor"]
    return valor_total

# Função para calcular o peso de uma solução


def calcular_peso(sol):
    peso_total = 0
    for i in range(len(sol)):
        if sol[i] == 1:
            peso_total += objetos[i]["peso"]
    return peso_total

# Função para verificar se uma solução é válida de acordo com as categorias aceitas


def solucao_valida(sol):
    categorias_presentes = set()
    for i in range(len(sol)):
        if sol[i] == 1:
            categorias_presentes.add(objetos[i]["categoria"])
    return categorias_presentes.issubset(set(categorias_aceitas))

# Função para gerar uma solução inicial aleatória


def gerar_solucao_inicial():
    sol = [random.randint(0, 1) for _ in range(len(objetos))]
    while not solucao_valida(sol):
        sol = [random.randint(0, 1) for _ in range(len(objetos))]
    return sol

# Função para fazer um movimento aleatório na solução


def fazer_movimento(sol):
    idx = random.randint(0, len(sol)-1)
    sol[idx] = 1 - sol[idx]  # Inverte o valor do objeto

# Função de aceitação baseada na diferença de valores


def funcao_aceitacao(valor_atual, valor_vizinho, temperatura):
    if valor_vizinho > valor_atual:
        return True
    else:
        probabilidade = pow(2.71, (valor_vizinho - valor_atual) / temperatura)
        return random.uniform(0, 1) < probabilidade

# Algoritmo Simulated Annealing


def simulated_annealing():
    solucao_atual = gerar_solucao_inicial()
    melhor_solucao = solucao_atual[:]
    melhor_valor = calcular_valor(melhor_solucao)
    temperatura = temperatura_inicial

    for i in range(numero_iteracoes):
        vizinho = solucao_atual[:]
        fazer_movimento(vizinho)

        if solucao_valida(vizinho):
            valor_atual = calcular_valor(solucao_atual)
            valor_vizinho = calcular_valor(vizinho)

            if funcao_aceitacao(valor_atual, valor_vizinho, temperatura):
                solucao_atual = vizinho[:]

                if valor_vizinho > melhor_valor:
                    melhor_solucao = solucao_atual[:]
                    melhor_valor = valor_vizinho

        temperatura *= fator_resfriamento

    return melhor_solucao


# Executando o algoritmo
melhor_solucao = simulated_annealing()

# Imprimindo a melhor solução encontrada
print("Melhor solução encontrada:")
for i in range(len(melhor_solucao)):
    if melhor_solucao[i] == 1:
        print("Objeto", i+1, " - Peso:", objetos[i]["peso"], " - Valor:",
              objetos[i]["valor"], " - Categoria:", objetos[i]["categoria"])
