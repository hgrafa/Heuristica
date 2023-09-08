class Item:
    def __init__(self, weight, value, available_compartiments):
        self.weight = weight
        self.value = value
        self.available_compartiments = available_compartiments

    def __str__(self):
        aux = f'Peso: {self.weight}, Valor: {self.value}'
        return aux
