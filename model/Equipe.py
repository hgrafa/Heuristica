import time
from model.Maquina import Maquina


def eh_maquina(elemento):
    return True if isinstance(elemento, Maquina) else False


class Equipe:

    # construtor
    def __init__(self, id,  disponibilidade, janela_final: list, janela_inicial: list):
        self.id = id
        self.disponibilidade = disponibilidade
        self.janela_final = janela_final.copy()
        self.janela_inicial = janela_inicial.copy()
        self.historico = []
        self.maquinas = []

    # ------------------------------------------

    @property
    def tempo_de_processamento(self):
        tempo_de_processamento = self.historico[-1]
        return tempo_de_processamento if tempo_de_processamento >= 0 else 0

    # ------------------------------------------

    @property
    def tempo_livre(self):
        disponibilidade = self.disponibilidade
        tempo_atual = self.historico[-1]  # pega o ultimo historico
        return disponibilidade - tempo_atual

    # ------------------------------------------

    def adiciona_maquina(self, nova_maquina):
        if not eh_maquina(nova_maquina):
            return

        janela_final_valida = self.esta_dentro_da_janela_final(nova_maquina)
        self.__ajusta_tempo_janela_final__(nova_maquina)

        if not janela_final_valida:
            return False

        # TODO ! continuar para janela inicial
        self.maquinas.append(nova_maquina)

    # ------------------------------------------

    def esta_dentro_da_janela_final(self, nova_maquina):
        janela_final = self.janela_final[nova_maquina.index]
        tempo_atual = self.tempo_de_processamento
        tempo_com_nova_maquina = tempo_atual + nova_maquina.tempo_processamento

        return tempo_com_nova_maquina <= janela_final

    # ------------------------------------------

    def __ajusta_janela_inicial__(self, nova_maquina):
        index = nova_maquina.index
        janela = nova_maquina.tempo_processamento
        horario_autorizado = self.janela_inicial[index]
        tempo_inicial = self.tempo_de_processamento

        # precisa esperar ?
        tempo_final = max(tempo_inicial, horario_autorizado) + janela
        tempo_de_espera = max(tempo_final - tempo_inicial, 0) - janela
        nova_maquina.tempo_de_espera = tempo_de_espera
        nova_maquina.janela_inicial = horario_autorizado
        self.historico.append(tempo_final)

    # ------------------------------------------

    def tabela_maquinas(self):
        aux = '| janela | ind. Ativ. | origem | Inicial | esperou | historico |\n'
        aux += '| :-: | :-: | :-: | :-: | :-: | :-: |\n'
        print(self.historico)

        cont = 0
        for maquina in self.maquinas:
            aux += str(maquina) + f' {self.historico[cont]}|\n'
            cont += 1

        aux += '\n'
        return aux

    # ------------------------------------------

    def __str__(self):
        id_equipe = self.id
        total = self.disponibilidade
        utilizado = self.tempo_de_processamento
        livre = self.disponibilidade - self.tempo_de_processamento

        return f"| {id_equipe} | {total} | {utilizado} | {livre}"
