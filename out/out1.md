# Heuristica

soma: 1 | config = [ X, X, X, ]

- disponibilidade: 30
- janela final: 27
- janela: 3
- espera: 3
- tempo_atual: 0
- tempo_com_maquina: 6
- pode inserir
------
- disponibilidade: 24
- janela final: 19
- janela: 3
- espera: 0
- tempo_atual: 6
- tempo_com_maquina: 9
- pode inserir
------
- disponibilidade: 21
- janela final: 25
- janela: 4
- espera: 0
- tempo_atual: 9
- tempo_com_maquina: 13
- pode inserir
------
- disponibilidade: 17
- janela final: 35
- janela: 1
- espera: 0
- tempo_atual: 13
- tempo_com_maquina: 14
- pode inserir
------
soma: 1 | config = [  , X, X, ]

- disponibilidade: 40
- janela final: 27
- janela: 1
- espera: 3
- tempo_atual: 0
- tempo_com_maquina: 4
- pode inserir
------
- disponibilidade: 36
- janela final: 19
- janela: 1
- espera: 0
- tempo_atual: 4
- tempo_com_maquina: 5
- pode inserir
------
- disponibilidade: 35
- janela final: 25
- janela: 1
- espera: 0
- tempo_atual: 5
- tempo_com_maquina: 6
- pode inserir
------
- disponibilidade: 34
- janela final: 35
- janela: 2
- espera: 1
- tempo_atual: 6
- tempo_com_maquina: 9
- pode inserir
------
soma: 1 | config = [  , X,  , ]

soma: 2 | config = [  , X,  , ]

- disponibilidade: 16
- janela final: 27
- janela: 2
- espera: 0
- tempo_atual: 14
- tempo_com_maquina: 16
- pode inserir
------
- disponibilidade: 14
- janela final: 19
- janela: 3
- espera: 0
- tempo_atual: 16
- tempo_com_maquina: 19
- pode inserir
------
- disponibilidade: 11
- janela final: 25
- janela: 1
- espera: 0
- tempo_atual: 19
- tempo_com_maquina: 20
- pode inserir
------
- disponibilidade: 10
- janela final: 35
- janela: 1
- espera: 0
- tempo_atual: 20
- tempo_com_maquina: 21
- pode inserir
------
soma: 2 | config = [  ,  ,  , ]



--------

Equipe | Total | Utilizado | Livre |
| :-: | :-: | :-: | :-: |
| 0 | 30 | 21 | 9
| 1 | 40 | 9 | 31

## Equipe 0
[6, 9, 13, 14, 16, 19, 20, 21]
| janela | ind. Ativ. | origem | Inicial | esperou | historico |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 3 | 0 | 0 | 3 | 3 | 6|
| 3 | 0 | 1 | 3 | 0 | 9|
| 4 | 0 | 2 | 4 | 0 | 13|
| 1 | 0 | 3 | 7 | 0 | 14|
| 2 | 1 | 0 | 3 | 0 | 16|
| 3 | 1 | 1 | 3 | 0 | 19|
| 1 | 1 | 2 | 4 | 0 | 20|
| 1 | 1 | 3 | 7 | 0 | 21|


## Equipe 1
[4, 5, 6, 9]
| janela | ind. Ativ. | origem | Inicial | esperou | historico |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 2 | 0 | 3 | 3 | 4|
| 1 | 2 | 1 | 3 | 0 | 5|
| 1 | 2 | 2 | 4 | 0 | 6|
| 2 | 2 | 3 | 7 | 1 | 9|


