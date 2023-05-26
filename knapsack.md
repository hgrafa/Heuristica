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
